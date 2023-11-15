class preprocessing_ops():
    def __init__(self, df):
        self.df = df

    def drop_duplicates(self): 
        self.df.drop_duplicates(inplace=True) 
    
    # since WT01 and WT02 both indicate fogs (only difference is if it's heavy or not), we can combine them into one column
    def add_fog(self):
        self.df['WT_FOG'] = np.where((self.df['WT01'] == 1) | (self.df['WT02'] == 1), 1, 0)
        self.df.drop(columns=['WT01','WT02'],inplace=True)

    def remove_cancelled(self):
        self.df = self.df[self.df.CANCELLED != 1]
        self.df.drop(columns=['CANCELLED','CANCELLATION_CODE'],inplace = True)

    def remove_missing_values(self):
        self.df = self.df.loc[:, self.df.isnull().mean() < .9]
    
    # drop IDs, similar columns, post-flight available columns, na values above 35%
    def drop_columns(self):
        self.df.drop(columns=['OP_CARRIER_FL_NUM','Unnamed: 32', 'ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID','AIRLINE_ID','OP_UNIQUE_CARRIER','STATION','MANUFACTURE_YEAR'
                         , 'ORIGIN_CITY_NAME','ORIGIN_CITY_NAME_x','ORIGIN_CITY_NAME_y','NAME_x','NAME_y','DEST_CITY_NAME','DEPARTING_AIRPORT','DISPLAY_AIRPORT_NAME','DEST_CITY_NAME'
                         , 'DATE', 'ACTUAL_ELAPSED_TIME','DEP_TIME','DEP_DELAY_NEW', 'DEP_TIME_BLK','ARR_TIME','ARR_DELAY_NEW','ARR_TIME_BLK'
                         , 'CARRIER_DELAY','WEATHER_DELAY','NAS_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY', 'WESD','PSUN','TSUN','SN32','SX32','TOBS','WT11','PGTM','SNWD','SNOW'
                         ] ,inplace = True)
    
    # WT has 1 unique value (1 if true and nan if not so filling nans with 0s). then deal with high percentage 0 columns
    def fill_weather_codes(self):
        self.df.fillna({'WT03':'0', 'WT04':'0', 'WT05':'0', 'WT06':'0', 'WT07':'0', 'WT08':'0', 'WT09':'0', 'WT10':'0'}, inplace=True)
        self.df.drop(columns=['WT10','WT07','WT05','WT09','WT04','WT06'],inplace=True)

    # ‘any’ : If any NA values are present, drop that row or column.
    def drop_na(self):
        self.df.dropna(subset=['TAVG','NUMBER_OF_SEATS','WDF5','WSF5','PRCP','TMIN','TMAX','AWND','WSF2','WDF2'], how='any',inplace=True)

    def get_df(self):
        return self.df   