#include <Python.h>
/**
 * print_python_list_info - print info about python lists.
 * @p: A pyobject list.
 *
 * Return: Nothing
 *
 * Description: print basic info about python lists.
 *
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyobject *odj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *) p)->allocated;

	printf("[*] size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(pbj)->tp_name);
	}
}
