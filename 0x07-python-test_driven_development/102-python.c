#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Print information about a Python string object.
 * @p: PyObject pointer to a Python string.
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		Py_UNICODE *str = PyUnicode_AS_UNICODE(p);
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);

		printf("[.] string object info\n");
		printf("  type: %s\n", Py_TYPE(p)->tp_name);
		printf("  length: %zd\n", length);
		printf("  value: %ls\n", str);
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
