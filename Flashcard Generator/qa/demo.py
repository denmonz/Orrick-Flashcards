import os
import pandas as pd
from ast import literal_eval
from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model
import warnings
from xl_ls import xl2ls
import xlsxwriter
import time
from question_filter import *

#from tensorflow.python.util import deprecation as deprecation
#deprecation._PRINT_DEPRECATION_WARNINGS = False

def demo():
	# Read pdf file and convert it to a specific dataframe
	# using the apple brief as demo
	df = pdf_converter(directory_path='./pdf/apple')

	'''
	# 
	# Download model
	# Don't run this, too long of a wait-time for clients
	# just provide and upload my trained models
	# download_model(model='bert-squad_1.1', dir='./models')
	'''

	# read BERT model into pipeline
	bert_qa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=3.0)
	# Option 2: read distilled bert model into pipeline
	# bert_qa_pipeline = QAPipeline(reader='./models/distilbert_qa.joblib', max_df=1.0)
	# Fit Retriever to documents
	bert_qa_pipeline.fit_retriever(df=df)

	# connect our question generator here
	temp = xl2ls(230)
	questions = []

	for ques in temp:
		questions.append(ques[0])


	# sample:
	'''
	questions = ['What does plaintiffs failed to meet',
				'What do Rule 23 petitions not automatically stay',
				'What did Rail Freight F. 3d at',
				'What U. S. at 473?',
				'What U. S. at 473']
	'''
	# save new answers and reference paragraphs in a list
	
	new_ans = []
	ref = []

	for i in range(50):#len(questions)):
		predictions = bert_qa_pipeline.predict(questions[i])
		new_ans.append(predictions[0])
		ref.append(predictions[2])
		#print('{} Question {} from {} {}'.format('-' * 10, i+1, predictions[1], '-' * 10))
		#print('Question: {}'.format(questions[i]))
		#print('Answer: {}'.format(predictions[0]))
		#print('Document Name: {}'.format(predictions[1]))
		#print('Reference Paragraph: "{}"\n'.format(predictions[2]))
	workbook = xlsxwriter.Workbook('Example2.xlsx')
	
	worksheet = workbook.add_worksheet()
	row, col = 0, 0
	for item in new_ans:
		worksheet.write(row, col, item)
		row += 1
	workbook.close()
	
	workbook2 = xlsxwriter.Workbook('Example3.xlsx')
	worksheet2 = workbook.add_worksheet()
	row1, col1 = 0, 0
	for item1 in ref:
		worksheet.write(row1, col1, item1)
		row1 += 1
	workbook2.close() 
	
	 


print(demo())

	
