# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Quiz(Document):


	def get_quiz(self):
		pass


	def evaluate(self, response_dict):
		self.get_questions()
		answers = {q.name:q.get_answer() for q in self.get_questions()}
		print(response_dict)
		print(type(response_dict))
		print(answers)
		print(type(answers))


	def get_questions(self):
		quiz_question = self.get_all_children()
		if quiz_question:
			questions = [frappe.get_doc('Question', question.question_link) for question in quiz_question]
			return questions
		else:
			return None

