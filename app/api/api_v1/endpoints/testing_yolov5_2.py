from fastapi.testclient import TestClient
from fastapi import status,HTTPException
#from fastapi_example.yolov5_endpoints import router
from app.api.api_v1.endpoints.yolov5_endpoints import router
from pathlib import Path

client = TestClient(router)


#def test_weight_upload():
    #print("#############################")
    #response = client.post("/uploadweights",headers={"file":"D:\DS-AI\algorithm_library\algorithm-library-api\model_weights\yolov5\yolov5s.pt"})
    #print("#############################",response.json())

def test_yolov5_weights():
    response=client.get("/weights")
    assert response.status_code==200
    assert response.json()==[Path(f).as_posix().rsplit('/', maxsplit=1)[-1].split('.')[0]
            for f in glob.glob("model_weights/yolov5/*.pt")]
            
def test_yolov5_upload_weights():
    url = "/uploadweights"
    filename='D:/DS-AI/algorithm_library/algorithm-library-api/model_weights/yolov5/yolov5s.pt'
    filename_="yolov5s.pt"
      
    up= {'file':(filename_, open(filename, 'rb'), 'application/octet-stream')}
    response=client.post(url,files=up)
    print("#############################",response.json())
    assert response.json== {'filename': filename_}
    
#if __name__ == '__main__':
  #  test_weight_upload()