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
	CustomerAcquisitions_DBFSs = DBFSConnector.DBFSConnector.fetch([], {}, "5e6b1e39be588d7717182ecd", spark, "{'url': '/Demo/CustomerAcquisitionTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi0ef076722999cf4cd8859e9aafdb7b76', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e6b1e39be588d7717182ecd','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b1e39be588d7717182ecd','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b1e39be588d7717182ece','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerAcquisitions_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e6b1e39be588d7717182ecd"],{"5e6b1e39be588d7717182ecd": CustomerAcquisitions_DBFSs}, "5e6b1e39be588d7717182ece", spark,json.dumps( {"FE": [{"transformationsData": {"feature_label": "City"}, "feature": "City", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "ARVADA", "max": "WHEAT RIDGE", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Product_Category"}, "feature": "Product_Category", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "Furniture", "max": "Technology", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Product_Sub-Category"}, "feature": "Product_Sub-Category", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "Appliances", "max": "Telephones and Communication", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Count", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "1.08", "stddev": "0.29", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Customer ID", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "1765.61", "stddev": "974.89", "min": "2", "max": "3394", "missing": "0"}}, {"transformationsData": {}, "feature": "Store Number", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "102.38", "stddev": "1.83", "min": "100", "max": "105", "missing": "0"}}, {"transformationsData": {"feature_label": "Customer Segment"}, "feature": "Customer Segment", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "Consumer", "max": "Small Business", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "First Name"}, "feature": "First Name", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "ADXXXX", "max": "YA", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Last Name"}, "feature": "Last Name", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "ABXXXXX", "max": "ZAXXXXXX", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Address"}, "feature": "Address", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "1003 WESTVIEW CT", "max": "9871 E WALSH PL", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "State"}, "feature": "State", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "CO", "max": "CO", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Zip", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "80114.33", "stddev": "105.02", "min": "80002", "max": "80602", "missing": "0"}}, {"transformationsData": {}, "feature": "DriveTime", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "651", "mean": "12.72", "stddev": "7.35", "min": "0.91", "max": "30.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Length of Residense", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "10.36", "stddev": "10.31", "min": "0", "max": "55", "missing": "0"}}, {"transformationsData": {}, "feature": "MOR BANK: UPSCALE MERCHANDISE BUYER", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "0.01", "stddev": "0.11", "min": "0", "max": "1", "missing": "0"}}, {"transformationsData": {"feature_label": "MOSAIC HOUSEHOLD"}, "feature": "MOSAIC HOUSEHOLD", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "A01", "max": "U00", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "MOSAIC DESCRIPTION"}, "feature": "MOSAIC DESCRIPTION", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "Aspirational Fusion", "max": "Young City Solos", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Customer_Lon", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "651", "mean": "-104.92", "stddev": "0.12", "min": "-105.226518", "max": "-104.65312", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Customer_Lat", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "651", "mean": "39.7", "stddev": "0.09", "min": "39.485121", "max": "39.998058", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Store ID", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "651", "mean": "102.38", "stddev": "1.83", "min": "100", "max": "105", "missing": "0"}}, {"transformationsData": {}, "feature": "Store_Lon", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "651", "mean": "-104.92", "stddev": "0.12", "min": "-105.077754", "max": "-104.717928", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Store_Lat", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "651", "mean": "39.7", "stddev": "0.08", "min": "39.565799", "max": "39.856274", "missing": "0"}, "transformation": ""}, {"transformationsData": {"feature_label": "Channel"}, "feature": "Channel", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "651", "mean": "", "stddev": "", "min": "Catalog", "max": "eCommerce", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "City_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "1.62", "stddev": "2.41", "min": "0.0", "max": "17.0", "missing": "0"}}, {"feature": "Product_Category_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "651", "mean": "0.63", "stddev": "0.8", "min": "0", "max": "2", "missing": "0"}}, {"feature": "Product_Sub-Category_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "5.2", "stddev": "4.31", "min": "0.0", "max": "16.0", "missing": "0"}}, {"feature": "Customer Segment_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "651", "mean": "1.24", "stddev": "1.11", "min": "0", "max": "3", "missing": "0"}}, {"feature": "First Name_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "65.58", "stddev": "61.08", "min": "0.0", "max": "230.0", "missing": "0"}}, {"feature": "Last Name_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "107.79", "stddev": "96.89", "min": "0.0", "max": "334.0", "missing": "0"}}, {"feature": "Address_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "211.71", "stddev": "158.66", "min": "0.0", "max": "513.0", "missing": "0"}}, {"feature": "State_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "651", "mean": "0.0", "stddev": "0.0", "min": "0", "max": "0", "missing": "0"}}, {"feature": "MOSAIC HOUSEHOLD_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "14.78", "stddev": "12.77", "min": "0.0", "max": "54.0", "missing": "0"}}, {"feature": "MOSAIC DESCRIPTION_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "651", "mean": "5.7", "stddev": "4.47", "min": "0.0", "max": "18.0", "missing": "0"}}, {"feature": "Channel_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "651", "mean": "0.51", "stddev": "0.69", "min": "0", "max": "2", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e6b1e39be588d7717182ece','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b1e39be588d7717182ece','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e6b1e39be588d7717182ecf','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
	CustomerAcquisitions_AutoML = tpot_execution.Tpot_execution.run(["5e6b1e39be588d7717182ece"],{"5e6b1e39be588d7717182ece": CustomerAcquisitions_AutoFE}, "5e6b1e39be588d7717182ecf", spark,json.dumps( {"model_type": "classification", "label": "Channel", "features": ["City", "Product_Category", "Product_Sub-Category", "Count", "Customer ID", "Store Number", "Customer Segment", "First Name", "Last Name", "Address", "State", "Zip", "DriveTime", "Length of Residense", "MOR BANK: UPSCALE MERCHANDISE BUYER", "MOSAIC HOUSEHOLD", "MOSAIC DESCRIPTION", "Customer_Lon", "Customer_Lat", "Store ID", "Store_Lon", "Store_Lat"], "percentage": "30", "executionTime": "5", "sampling": "1", "sampling_value": "over", "run_id": "", "model_id": "5e6b2bf6be588d7717182ff8", "ProjectName": "ML Sample Problems", "PipelineName": "CustomerAcquisitions", "pipelineId": "5e6b1e39be588d7717182ecc", "userid": "5df78f4be2f2eff24740bbd7", "runid": "", "url_ResultView": "http://13.68.212.36:3200", "experiment_id": "480623611921769"}))

	PipelineNotification.PipelineNotification().completed_notification('5e6b1e39be588d7717182ecf','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e6b1e39be588d7717182ecf','5df78f4be2f2eff24740bbd7','http://13.68.212.36:3200/pipeline/notify','http://13.68.212.36:3200/logs/getProductLogs')
	sys.exit(1)

