import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b1e39be588d7717182ecd','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerAcquisitions_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e6b1e39be588d7717182ecd", spark, "{'url': '/Demo/CustomerAcquisitionTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi0ef076722999cf4cd8859e9aafdb7b76', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e6b1e39be588d7717182ecd','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b1e39be588d7717182ecd','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b1e39be588d7717182ece','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerAcquisitions_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e6b1e39be588d7717182ecd"],{"5e6b1e39be588d7717182ecd": CustomerAcquisitions_DBFS}, "5e6b1e39be588d7717182ece", spark,json.dumps( {"FE": [{"transformationsData": {"feature_label": "City"}, "feature": "City", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "ARVADA", "max": "WHEAT RIDGE", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Product_Category"}, "feature": "Product_Category", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "Furniture", "max": "Technology", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Product_Sub-Category"}, "feature": "Product_Sub-Category", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "Appliances", "max": "Telephones and Communication", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Count", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "1.08", "stddev": "0.3", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Customer ID", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "1755.82", "stddev": "944.21", "min": "2", "max": "3402", "missing": "0"}}, {"transformationsData": {}, "feature": "Store Number", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "102.37", "stddev": "1.81", "min": "100", "max": "105", "missing": "0"}}, {"transformationsData": {"feature_label": "Customer Segment"}, "feature": "Customer Segment", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "Consumer", "max": "Small Business", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "First Name"}, "feature": "First Name", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "AAXXX", "max": "ZEXXX", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Last Name"}, "feature": "Last Name", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "ABXXXX", "max": "ZIXXXXXXX", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Address"}, "feature": "Address", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "10 MEADOW ROSE LN", "max": "9924 W ARLINGTON AVE", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "State"}, "feature": "State", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "CO", "max": "CO", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Zip", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "80112.74", "stddev": "102.27", "min": "80002", "max": "80602", "missing": "0"}}, {"transformationsData": {}, "feature": "DriveTime", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2325", "mean": "13.1", "stddev": "7.31", "min": "0.65", "max": "30.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Length of Residense", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "10.98", "stddev": "10.75", "min": "0", "max": "55", "missing": "0"}}, {"transformationsData": {}, "feature": "MOR BANK: UPSCALE MERCHANDISE BUYER", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "0.01", "stddev": "0.15", "min": "0", "max": "4", "missing": "0"}}, {"transformationsData": {"feature_label": "MOSAIC HOUSEHOLD"}, "feature": "MOSAIC HOUSEHOLD", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "A01", "max": "U00", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "MOSAIC DESCRIPTION"}, "feature": "MOSAIC DESCRIPTION", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "Aspirational Fusion", "max": "Young City Solos", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Customer_Lon", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2325", "mean": "-104.92", "stddev": "0.12", "min": "-105.226518", "max": "-104.65312", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Customer_Lat", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2325", "mean": "39.69", "stddev": "0.09", "min": "39.433416", "max": "39.998058", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Store ID", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "2325", "mean": "102.37", "stddev": "1.81", "min": "100", "max": "105", "missing": "0"}}, {"transformationsData": {}, "feature": "Store_Lon", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2325", "mean": "-104.92", "stddev": "0.12", "min": "-105.077754", "max": "-104.717928", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Store_Lat", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "2325", "mean": "39.7", "stddev": "0.08", "min": "39.565799", "max": "39.856274", "missing": "0"}, "transformation": ""}, {"transformationsData": {"feature_label": "Channel"}, "feature": "Channel", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "2325", "mean": "", "stddev": "", "min": "Catalog", "max": "eCommerce", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "City_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "1.59", "stddev": "2.28", "min": "0.0", "max": "17.0", "missing": "0"}}, {"feature": "Product_Category_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2325", "mean": "0.64", "stddev": "0.79", "min": "0", "max": "2", "missing": "0"}}, {"feature": "Product_Sub-Category_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "5.08", "stddev": "4.27", "min": "0.0", "max": "16.0", "missing": "0"}}, {"feature": "Customer Segment_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2325", "mean": "1.24", "stddev": "1.11", "min": "0", "max": "3", "missing": "0"}}, {"feature": "First Name_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "77.44", "stddev": "77.37", "min": "0.0", "max": "339.0", "missing": "0"}}, {"feature": "Last Name_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "152.09", "stddev": "140.56", "min": "0.0", "max": "552.0", "missing": "0"}}, {"feature": "Address_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "377.85", "stddev": "305.1", "min": "0.0", "max": "1105.0", "missing": "0"}}, {"feature": "State_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2325", "mean": "0.0", "stddev": "0.0", "min": "0", "max": "0", "missing": "0"}}, {"feature": "MOSAIC HOUSEHOLD_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "15.05", "stddev": "13.31", "min": "0.0", "max": "58.0", "missing": "0"}}, {"feature": "MOSAIC DESCRIPTION_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "2325", "mean": "5.84", "stddev": "4.63", "min": "0.0", "max": "19.0", "missing": "0"}}, {"feature": "Channel_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "2325", "mean": "0.48", "stddev": "0.67", "min": "0", "max": "2", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e6b1e39be588d7717182ece','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b1e39be588d7717182ece','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b1e39be588d7717182ecf','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerAcquisitions_AutoML = tpot_execution.Tpot_execution.run(["5e6b1e39be588d7717182ece"],{"5e6b1e39be588d7717182ece": CustomerAcquisitions_AutoFE}, "5e6b1e39be588d7717182ecf", spark,json.dumps( {"model_type": "classification", "label": "Channel", "features": ["City", "Product_Category", "Product_Sub-Category", "Count", "Customer ID", "Store Number", "Customer Segment", "First Name", "Last Name", "Address", "State", "Zip", "DriveTime", "Length of Residense", "MOR BANK: UPSCALE MERCHANDISE BUYER", "MOSAIC HOUSEHOLD", "MOSAIC DESCRIPTION", "Customer_Lon", "Customer_Lat", "Store ID", "Store_Lon", "Store_Lat"], "percentage": "70", "executionTime": "5", "sampling": "1", "sampling_value": "over", "run_id": "", "model_id": "5e6b2112be588d7717182f2c", "ProjectName": "ML Sample Problems", "PipelineName": "CustomerAcquisitions", "pipelineId": "5e6b1e39be588d7717182ecc", "userid": "5df78f4be2f2eff24740bbd7", "runid": "", "url_ResultView": "http://13.68.212.36:3200", "experiment_id": "480623611921769"}))

	PipelineNotification.PipelineNotification().completed_notification('5e6b1e39be588d7717182ecf','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b1e39be588d7717182ecf','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)

