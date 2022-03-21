from fastapi.testclient import TestClient
from fastapi import status,HTTPException, File, UploadFile
#from fastapi_example.yolov5_endpoints import router
from app.api.api_v1.endpoints.yolov5_endpoints import router
import glob
from pathlib import Path
client = TestClient(router)


def test_yolov5_weights():
    response = client.get("/weights")
    #response = client.post("/uploadweights",headers={"file":"D:\DS-AI\algorithm_library\algorithm-library-api\model_weights\yolov5\yolov5s.pt"})
    print("#############################",response.json())
    return response
    #----- write for get method and test response


def test_upload_weights():
    url = "/uploadweights"
    filename='D:/DS-AI/algorithm_library/algorithm-library-api/model_weights/yolov5/yolov5s.pt'
    filename_="yolov5s.pt"
      
    up= {'file':(filename_, open(filename, 'rb'), 'application/octet-stream')}
    response=client.post(url,files=up)
    print("#############################",response.json())
    assert response.json()== {'filename': filename_}
def test_main():
    response=client.get("/")
    print("############################# response main ",response.json())
    return response.json()
    #assert response.json()
    
    
def test_yolov5_detect():
    url = "/detect"
    # filename='D:/DS-AI/tox_auto_sample/images/example1.png'
    # filename_='example1.png'
    # up= [{'files':(filename_, open(filename, 'rb'), 'image/png')}]
    # up_= [{'files':(filename_, open(filename, 'rb'), 'image/png')},{'files':(filename_, open(filename, 'rb'), 'image/png')}]
    # upp={'files':(filename_, open(filename, 'rb'), 'image/png')}
    
    # f=[('files', open(filename, 'rb')),('files',open('D:/DS-AI/tox_auto_sample/images/example2.png','rb'))]
    # upp_=[{'files':[(filename_, open(filename, 'rb'), 'image/png'),(filename_, open(filename, 'wb'), 'image/png')]}]
    
    # files_ = [('files', open(filename, 'rb')), ('files', open(filename, 'rb'))]
    # multiple_files =[
    # ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
    # ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
    
    multiple_files_ =[
    ('files', ('example1.png', open('D:/DS-AI/tox_auto_sample/images/example1.png', 'rb'), 'image/png')),
    ('files', ('example2.png', open('D:/DS-AI/tox_auto_sample/images/example2.png', 'rb'), 'image/png'))]
    
    
    # path = glob.glob('D:/DS-AI/tox_auto_sample/images/*', recursive=True) # images' path
    # lst_img = []
    # for p in path[:3]:
        # lst_img.append({'files', open(p, 'rb')})
    # data=['files'=multiple_files_,'weights'='yolov5s']
    response=client.post(url,files=multiple_files_)
    print("#############################",response.json())
    
    
    
if __name__ == '__main__':
    
    print(test_yolov5_weights())
    
    print(test_upload_weights())
    print(test_yolov5_detect())
    #print(test_main())
    #test_upload()