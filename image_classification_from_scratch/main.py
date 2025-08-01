from PIL import Image
import math
import time
class ImageClassify:
    def __init__(self):
        pass
    def _image_to_vector(self,image_path:str,target_size:tuple|None,flatten=True):
        s=time.time()
        image = Image.open(image_path).convert('RGB')
        image = image.resize(target_size,Image.LANCZOS)
        width, height = image.size
        pixels = list(image.getdata())
        normalized_pixels = [(round(r/255.0,3),round(g/255.0,3),round(b/255.0,3)) for (r,g,b) in pixels]
        if flatten:
            print(f"image to vector time: {(time.time()-s)*1e3}")
            return [value for pixel in normalized_pixels for value in pixel]
            #return [p / 255.0 for p in pixels]
        # else:
        #     return [normalized_pixels[i*width:(i+1)*width] for i in range(height)]
    def _magnitude(self,v:list)->float:
        s=time.time()
        vlength = len(v)
        sum_squares=0
        for value in range(vlength):
            sum_squares+=(v[value]**2)
        print(f"magnitude time: {(time.time()-s)*1e3}")
        return math.sqrt(sum_squares)
    def _dot_product(self,va:list,vb:list)->float:
        s=time.time()
        p=0
        vlen=len(va)
        if len(va)!=len(vb):
            raise ValueError("Error: vector inputs must be of equal size")
        for value in range(vlen):
            p+=(va[value]*vb[value])
        print(f"dot product time: {(time.time()-s)*1e3}")
        return p
    def _cosine_theta(self,va:list,vb:list)->float:
        s=time.time()
        mag_a,mag_b = self._magnitude(va), self._magnitude(vb)
        dotp = self._dot_product(va,vb)
        print(f"cos theta time: {(time.time()-s)*1e3}")
        return dotp/(mag_a*mag_b)
    
classify = ImageClassify()
if __name__=="__main__":
    start_time = time.time()
    va=classify._image_to_vector(image_path="photos/forest.jpg",target_size=(16,16),flatten=True)
    vb=classify._image_to_vector(image_path="photos/cat.jpeg",target_size=(16,16),flatten=True)
    with open("forest_vector.txt","w") as f:
        f.write(str(va))
    with open("cat_vector.txt","w") as f:
        f.write(str(vb))
    costheta = classify._cosine_theta(va,vb)
    duration = ((time.time()-start_time)*1e3,"ms")
    print(costheta)
    print(f"time: {duration}")
