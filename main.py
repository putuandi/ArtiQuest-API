from fastapi import FastAPI, File, UploadFile
from PIL import Image
from schemas.artifact import Artifact
from config.db import con
from models.index import artifacts
import tensorflow as tf
import numpy as np
import io

app = FastAPI()

class_mapping = {'cepuk':0, 'piring keramik':1, 'pis bolong':2}

@app.post("/api/artifacts/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Model dari ML
        model_path = "SavedModel/artiquest-object-identifier-3-fix.h5"
        # Memuat model
        loaded_model = tf.keras.models.load_model(model_path)
        # Membaca file gambar yang diunggah
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        image = image.resize((224, 224))
        image_array = np.array(image)
        input_data = np.expand_dims(
            image_array, axis=0).astype(np.float32) / 255.0

        # Melakukan prediksi menggunakan model
        predictions = loaded_model.predict(input_data)
        predicted_class_index = np.argmax(predictions).tolist()
        predicted_class = list(class_mapping.keys())[list(class_mapping.values()).index(predicted_class_index)]
        # confidence = predictions[0][predicted_class_index]

        return {"id_class": int(predicted_class_index), "predicted_class": predicted_class}
    except Exception as e:
         return {"message": f"Error: {e}"}, 400



""" # menampilkan semua data
@app.get('/api/allArtifacts')
async def all_artifacts():
    data=con.execute(artifacts.select()).fetchall()
    return {
        "success": True,
        "data":data
    } """
    
# menampilkan semua data
@app.get('/api/allArtifacts')
async def all_artifacts():
    data=con.execute(artifacts.select())
    result = data.fetchall()

    for i, res in enumerate(result):
        result[i] = {'id': res[0], 'name': res[1], 'description': res[2], 'image1': res[3], 'image2': res[4], 'image3': res[5],'location':res[6], 'lat': res[7], 'lon': res[8]}
    print(result)
    return {
        "success": True,
        "data": result
    }
    
    
# menampilkan data berdasarkan id
""" @app.get('/api/artifacts/{id}')
async def data_by_id(id:int):
    data=con.execute(artifacts.select().where(artifacts.c.id==id)).fetchall()
    return {
        "success": True,
        "data":data
    } """

@app.get('/api/artifacts/{id}')
async def data_by_id(id:int):
    data=con.execute(artifacts.select().where(artifacts.c.id==id))
    result = data.fetchall()
    result[0] = {'id': result[0][0], 'name': result[0][1], 'description': result[0][2], 'image1': result[0][3], 'image2': result[0][4], 'image3': result[0][5],'location': result[0][6], 'lat': result[0][7], 'lon': result[0][8]}
    print(result)
    
    return {
        "success": True,
        "data": result[0]
    }
    
    
# insert data
@app.post('/api/artifacts')
async def insert(artifact:Artifact):
    data=con.execute(artifacts.insert().values(
        name=artifact.name,
        description=artifact.description,
        image1=artifact.image1,
        image2=artifact.image2,
        image3=artifact.image3,
        location=artifact.location,
        lat=artifact.lat,
        lon=artifact.lon,
    ))

    # con.commit()
    # con.close()

    if data.is_insert:
        return {
            "success": True,
            "msg":"Artifact Insert Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }
    
    
         
    
# update data
@app.put('/api/artifacts/{id}')
async def update(id:int,artifact:Artifact):
    data=con.execute(artifacts.update().values(
        name=artifact.name,
        description=artifact.description,
        image1=artifact.image1,
        image2=artifact.image2,
        image3=artifact.image3,
        location=artifact.location,
        lat=artifact.lat,
        lon=artifact.lon,
    ).where(artifacts.c.id==id))

    # con.commit()
    # con.close()

    if data:
        return {
            "success": True,
            "msg":"Student Update Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }
         
    
         
# delete data
@app.delete('/api/artifacts/{id}')
async def delete(id:int):
    data=con.execute(artifacts.delete().where(artifacts.c.id==id))
    
    # con.commit()
    # con.close()

    if data:
        return {
            "success": True,
            "msg":"Student Delete Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }
         
    
         
# search data
@app.get('/api/artifacts/search/{search}')
async def search(search):
    data=con.execute(artifacts.select().where(artifacts.c.name.like('%'+search+'%')))
    result = data.fetchall()
    
    for i, res in enumerate(result):
        result[i] = {'id': res[0], 'name': res[1], 'description': res[2], 'image1': res[3], 'image2': res[4], 'image3': res[5], 'location': res[6], 'lat': res[7], 'lon': res[8]}
    print(result)
    
    return {
        "success": True,
        "data": result
    }
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080)