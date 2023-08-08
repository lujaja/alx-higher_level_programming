#include "lists.h"
/**
 * check_cycle - function
 *
 * @list: parameter
 * Return 1 if circular, 0 if not 
 *
 * Description: c function to check if a singly linked has a cycle in it
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;
	if (!list)
		return (0);

	ptr = list->next;

	while (ptr)
	{
		if (ptr == list)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
