import mysql.connector
from mysql.connector import Error
from datetime import datetime

class VehicleDB:
    def __init__(self) -> None:
        # 设置数据库连接参数
        self.db_config = {
            'host': 'localhost',
            'database': 'vehicles',
            'user': 'root',
            'password': 'abcd123$'
        }
        self.coordinate_table_name="coordinates_with_utc_timestamp"
            
    def connect_db(self):

        # 创建数据库连接
        try:
            self.connection = mysql.connector.connect(**self.db_config)

            if self.connection.is_connected():
                self.cursor = self.connection.cursor()

                # 创建存储经纬度和ENU坐标的表，包含 timestamp 字段
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS coordinates_with_utc_timestamp (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    uuid Varchar(20) NOT NULL,
                    timestamp DECIMAL(17,0) NOT NULL,
                    latitude DECIMAL(10, 8) NOT NULL,
                    longitude DECIMAL(11, 8) NOT NULL,
                    enu_x DECIMAL(10, 5) NOT NULL,
                    enu_y DECIMAL(10, 5) NOT NULL,
                    enu_z DECIMAL(10, 5) NOT NULL
                );
                '''
                self.cursor.execute(create_table_query)
                print("Table created successfully")

        except Error as e:
            print("Error:", e)

        finally:
            pass
        
    def disconnet_db(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection closed")
            
    def create_table(self):
        try:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS coordinates_with_utc_timestamp (
                id INT AUTO_INCREMENT PRIMARY KEY,
                uuid Varchar(20) NOT NULL,
                timestamp DECIMAL(17,0) NOT NULL,
                latitude DECIMAL(10, 8) NOT NULL,
                longitude DECIMAL(11, 8) NOT NULL,
                enu_x DECIMAL(10, 5) NOT NULL,
                enu_y DECIMAL(10, 5) NOT NULL,
                enu_z DECIMAL(10, 5) NOT NULL
            );
            '''
            self.cursor.execute(create_table_query)
            print("Table created successfully")
        except Error as e:
            print("Error:", e)
        finally:
            pass

    def delete_table(self):
        delete_table_query = f"DROP TABLE IF EXISTS {self.coordinate_table_name}"
        self.cursor.execute(delete_table_query)
        self.connection.commit

    def add_data_targets(self,targets):
        try:
                # 插入经纬度和ENU坐标数据，使用给定的 UTC timestamp
                insert_data_query = '''
                INSERT INTO coordinates_with_utc_timestamp (uuid,timestamp,latitude, longitude, enu_x, enu_y, enu_z) VALUES (%s,%s, %s, %s, %s, %s, %s);
                '''
                # data_to_insert = [
                #     (20231128180613282,40.7128, -74.0060, 100, 200, 50),
                #     (20231128180613282,34.0522, -118.2437, 150, 250, 60),
                #     (20231128180613282,41.8781, -87.6298, 120, 220, 40, )
                # ]
                data_to_insert=[]
                for target in targets:
                    enu_list=list(target.enu)
                    data_to_insert.append((target.uuid,target.utctime,target.latitude,target.longitude,enu_list[0],enu_list[1],enu_list[2]))

                self.cursor.executemany(insert_data_query, data_to_insert)

                self.connection.commit()
                # print("Data inserted successfully")

                # # 查询经纬度和ENU坐标数据，包含 timestamp
                # select_data_query = '''
                # SELECT * FROM coordinates_with_utc_timestamp;
                # '''
                # self.cursor.execute(select_data_query)
                # rows = self.cursor.fetchall()

                # print("Coordinates and ENU from table:")
                # for row in rows:
                #     print("ID:", row[0])
                #     print("Timestamp:", row[1])
                #     print("Latitude:", row[2])
                #     print("Longitude:", row[3])
                #     print("ENU_X:", row[4])
                #     print("ENU_Y:", row[5])
                #     print("ENU_Z:", row[6])
                #     print()
        except Error as e:
            print("Error:", e)

        finally:
            pass
            # print("data added")
        
    def add_data(self,target):
        try:
                # 插入经纬度和ENU坐标数据，使用给定的 UTC timestamp
                insert_data_query = '''
                INSERT INTO coordinates_with_utc_timestamp (uuid,timestamp,latitude, longitude, enu_x, enu_y, enu_z) VALUES (%s,%s, %s, %s, %s, %s, %s);
                '''
                # data_to_insert = [
                #     (20231128180613282,40.7128, -74.0060, 100, 200, 50),
                #     (20231128180613282,34.0522, -118.2437, 150, 250, 60),
                #     (20231128180613282,41.8781, -87.6298, 120, 220, 40, )
                # ]
                enu_list=list(target.enu)
                data_to_insert=[
                    (target.uuid,target.utctime,target.latitude,target.longitude,enu_list[0],enu_list[1],enu_list[2])
                ]

                self.cursor.executemany(insert_data_query, data_to_insert)

                self.connection.commit()
                # print("Data inserted successfully")

                # # 查询经纬度和ENU坐标数据，包含 timestamp
                # select_data_query = '''
                # SELECT * FROM coordinates_with_utc_timestamp;
                # '''
                # self.cursor.execute(select_data_query)
                # rows = self.cursor.fetchall()

                # print("Coordinates and ENU from table:")
                # for row in rows:
                #     print("ID:", row[0])
                #     print("Timestamp:", row[1])
                #     print("Latitude:", row[2])
                #     print("Longitude:", row[3])
                #     print("ENU_X:", row[4])
                #     print("ENU_Y:", row[5])
                #     print("ENU_Z:", row[6])
                #     print()
        except Error as e:
            print("Error:", e)

        finally:
            pass
            # print("data added")
            
    def get_vehicle_uuid_list(self):
        
        select_vehicle_uuids_query = f"SELECT DISTINCT uuid FROM {self.coordinate_table_name}"
        # 执行查询
        self.cursor.execute(select_vehicle_uuids_query)
        
        uuid_list = [row[0] for row in self.cursor.fetchall()]
        return uuid_list
        
    def get_trajectory_timestamp_range(self,timestamp0,timestamp1):
        # 查询在给定时间戳范围内的所有坐标点的 SQL 语句
        select_coordinates_query = f"SELECT uuid, MAX(timestamp) AS max_timestamp FROM {self.coordinate_table_name} WHERE timestamp BETWEEN %s AND %s GROUP BY uuid"
        self.cursor.execute(select_coordinates_query, (timestamp0, timestamp1))
        coordinates = self.cursor.fetchall()
        
        uuids=[]
        for coordinate in coordinates:
            uuids.append(coordinate[0])
        return uuids
    
    def get_trajectory_uuid_timestampe_range(self,uuid,timestamp0,timestamp1):
        select_coordinates_query = f"SELECT uuid,timestamp,enu_x, enu_y FROM {self.coordinate_table_name} WHERE uuid = %s AND timestamp BETWEEN %s AND %s"
        self.cursor.execute(select_coordinates_query, (uuid,timestamp0, timestamp1))
        coordinates = self.cursor.fetchall()
        
        # 打印轨迹坐标点
        trajectory=[]
        print(f"轨迹 {uuid} 的在timestamp {timestamp0}和{timestamp1}之间的点:")
        trajectory=[]
        for coordinate in coordinates:
            pt=[coordinate[0],int(coordinate[1]),float(coordinate[2]),float(coordinate[3])]
            trajectory.append(pt)
        return trajectory
    
    
    def get_trajectory_uuid(self,uuid):
        
        # 查询给定轨迹 UUID 的所有坐标点的 SQL 语句
        select_coordinates_query = f"SELECT uuid,timestamp,enu_x, enu_y FROM {self.coordinate_table_name} WHERE uuid = %s"

        # 执行查询
        self.cursor.execute(select_coordinates_query, (uuid,))
        coordinates = self.cursor.fetchall()
        
        # 打印轨迹坐标点
        trajectory=[]
        print(f"轨迹 {uuid} 的所有坐标点:")
        trajectory=[]
        for coordinate in coordinates:
            pt=[]
            pt.append(coordinate[0])
            pt.append(int(coordinate[1]))
            pt.append(float(coordinate[2]))
            pt.append(float(coordinate[3]))
            trajectory.append(pt)
            # print(f"坐标点: ({coordinate[1]}, {coordinate[2]})")
        return trajectory
    
    
def main():
    vehicle_db=VehicleDB()
    vehicle_db.connect_db()
    target=1
    vehicle_db.add_data(target)
    vehicle_db.get_vehicle_uuid()
    pass
        
if __name__ == "__main__":
    main()
