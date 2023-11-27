import pymap3d as pm
class Geographic:
    def __init__(self) -> None:
        self.lat0=30.88870163
        self.lon0=121.92311037
        self.h0=16.3946
        
# 30.88870163,121.92311037,16.3946
        
    def setOriLlh(self,lat0,lon0,h0):
        self.lat0,self.lon0,self.h0=lat0,lon0,h0
    
    def llh2enu(self, llh):
        lat, lon, h = llh
        return pm.geodetic2enu(lat, lon, h, self.lat0, self.lon0, self.h0)
    
    def enu2llh(self,enu):
        return pm.enu2geodetic(enu[0],enu[1],enu[2],self.lat0, self.lon0, self.h0)
        
def main():
    # Example usage:
    llh=[30.88365912,121.93665448,100]
    geographic=Geographic()
    geographic.llh2enu(llh)

if __name__ == "__main__":
    main()