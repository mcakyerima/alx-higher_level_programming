#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: A pointer to the Python list object
 */

void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);
		for (Py_ssize_t i = 0; i < size; i++)
		{
			PyObject *element = PyList_GET_ITEM(p, i);

			printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
		}
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
	}
}
