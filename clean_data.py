import pandas as pd

filepath_og = 'vehicle_registration_info.csv'
dtype = {'oid': str, 'laden_weight': str, 'mobile_number': str, 'nationality': str, 'no_of_axle': str, 'owner_address': str, 'owner_name': str, 'registration_date': str, 'registration_number': str, 'registration_office_name': str, 'seating_capacity': str,'series_oid': str, 'tax_token_exp_date': str, 'tax_token_issue_date': str, 'unladen_weight': str, 'updated_by': str, 'updated_on': str, 'vehiclecc': str, 'vehicle_class': str, 'vehicle_colour': str, 'vehicle_number': str, 'vehicle_registration_number': str, 'vehicle_series': str, 'vehicle_type': str, 'zone_oid': str, 'bridge_oid': str,'user_oid': str
}
vehicle_registration_data = pd.read_csv(filepath_og, on_bad_lines='skip', index_col= 'oid', dtype = dtype)

# convert joint_owner to boolean
vehicle_registration_data['joint_owner'] = vehicle_registration_data['joint_owner'].map({'YES': True, 'NO': False})


# drop columns with no useful information
columns_to_drop = ['created_on', 'father_husbend_name', 'request_key','response_time','response_time_epoch']

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
filepath_clean = 'vehicle_registration_info_clean.csv'
vehicle_registration_data_clean.to_csv(filepath_clean)

