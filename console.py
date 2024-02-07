#!/usr/bin/python3
""" module for python command line interpreter """
import cmd
import sys
import importlib
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
	"""
	class initiates command loop
	handles various functions for manipulating objects
	"""
	prompt = '(hbnb) '
	__classes = {
		"BaseModel": BaseModel,
		"User": User,
		"State": State,
		"Place": Place,
		"City": City,
		"Amenity": Amenity,
		"Review": Review
	}

	def do_quit(self, arg):
		""" quit method quits interpreter """
		exit()

	def do_EOF(self, arg):
		"""end of file method exits interpreter"""
		print()
		exit()

	def emptyline(self):
		"""Empty line"""
		pass

	def default(self, line: str):
		"""sanitizes input line and stores it"""
		self.line = line.strip()

	def input_check(self):
		""" return sanitized line to check input"""
		if self.line:
			return self.line
		pass

	def help_quit(self):
		""" help message for quit method"""
		print("Exit the interpreter")

	def do_create(self, arg):
		"""Create new instance of BaseModel"""
		args = arg.split()
		if len(args) < 1:
			print("** class name missing **")
			return
		class_name = args[0]
		if class_name not in self.__classes:
			print("** class doesn't exist **")
			return
		new_instance = self.__classes[class_name]()
		new_instance.save()
		print(new_instance.id)

	def do_show(self, arg):
		"""Show string representation of created instance"""
		args = arg.split()
		if len(args) < 1:
			print("**class name missing **")
			return
		if len(args) < 2:
			print("** instance id missing **")
			return
		class_name = args[0]
		instance_id = args[1]
		if class_name not in self.__classes:
			print("** class doesn't exist **")
			return
		all_obj = storage.all()
		key = "{}.{}".format(class_name, instance_id)
		if key in all_obj:
			instance = all_obj[key]
			print (instance)
		else:
			print ("** no instance found **")

	def do_destroy(self, arg):
		"""delete instance"""
		args = arg.split()
		if len(args) < 1:
			print("** class name missing **")
			return
		if len(args) < 2:
			print("** instance id missing **")
			return
		class_name = args[0]
		instance_id = args[1]
		try:
			module = importlib.import_module('models.base_model')
			class_ = getattr(module, class_name)
		except AttributeError:
			print("** class doesn't exist **")
			return
		all_obj = storage.all()
		key_delete = "{}.{}".format(class_name, instance_id)
		for key in all_obj.keys():
			if key.startswith(key_delete):
				del all_obj[key]
				break
		else:
			print ("** no instance found **")

	def do_all(self, arg):
		"""print all instances"""
    args = arg.split()
		if len(args) < 1:
			print ("** class name missing **")
			return
		class_name = args[0]
		if class_name not in self.__classes:
			print ("** class doesn't exist **")
			return
		all_obj = storage.all()
		instances = [obj for key, obj in all_obj.items() if key.split('.')[0] == class_name]
		if instances:
			for instance in instances:
				print (instance)
		else:
			print ("** no instances found **")

	def do_update(self, arg):
		"""update instance according to verified input"""
		objs = storage.all()
		args = arg.split()
		if len(args) >=4:
			class_name = args[0]
			obj_id = args[1]
			attribute = args[2]
			value = args[3]
			if class_name not in self.__classes:
				if obj_id in objs:
					if attribute not in ['id', 'created_at', 'updated_at']:
						if hasattr(objs[obj_id], attribute):
							atty_type = type(getattr(objs[obj_id], attribute))
							new_value = atty_type(value)
							setattr(objs[obj_id], attribute, new_value)
							objs[obj_id].save()
						else:
							print("** attribute name missing **")
							return
					else:
						print("** attribute cannot be updated **")
						return
				else:
					print("** no instance found **")
					return
			else:
				print("** class doesn't exist **")
				return
		elif len(args) == 3:
			print("** value missing **")
			return
		elif len(args) == 2:
			print("** attribute name missing **")
			return
		elif len(args) == 1:
			print("** instance id missing **")
			return
		else:
			print("** class name missing **")
			return

if __name__ == '__main__':
	HBNBCommand().cmdloop()
