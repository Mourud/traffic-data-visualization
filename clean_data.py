import pandas as pd

filepath_og = 'vehicle_registration_info.csv'
dtype = { 'mobile_number': str}
vehicle_registration_data = pd.read_csv(filepath_og, on_bad_lines='skip', index_col= 'oid', dtype = dtype)

# convert joint_owner to boolean
vehicle_registration_data['joint_owner'] = vehicle_registration_data['joint_owner'].map({'YES': True, 'NO': False})


# drop columns with no useful information
'''
updated_by: mostly null
updated_on: mostly null


is request key the license plate number???
'''
columns_to_drop = ['created_on', 'father_husbend_name', 'request_key','response_time','response_time_epoch', 'updated_by', 'updated_on',
                   'bridge_oid', 'user_oid'] # Mostly null

# drop columns with only one value
for col in vehicle_registration_data.columns:
    caridinality = vehicle_registration_data[col].nunique()
    if caridinality < 10:
        # print(col, ": ", caridinality )
        # print(vehicle_registration_data[col].unique())
        if caridinality == 1:
            columns_to_drop.append(col)
vehicle_registration_data_clean = vehicle_registration_data.drop(columns_to_drop, axis=1)





# save data
filepath_clean = 'output_vehicle_registration_info_clean.csv'
vehicle_registration_data_clean.to_csv(filepath_clean)

