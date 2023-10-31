#define PY_SSIZE_T_CLEAN
#include <Python.h>
/**
 * print_python_string - Prints python string
 * @p: Pointer to python object
 *
 * Returns: Nothing
 */

void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		Py_UNICODE *str = PyUnicode_AS_UNICODE(p);
		Py_ssize_t length = PyUnicode_GET_SIZE(p);

		printf("[.] string object info\n");
		printf("  type: %s\n", Py_TYPE(p)->tp_name);
		printf("  length: %zd\n", length);
		printf("  value: %ls\n", str);
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "object is not a string");
		PyErr_Print();
	}
}
