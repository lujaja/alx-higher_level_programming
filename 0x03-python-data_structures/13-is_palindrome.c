#include "lists.h"
/**
 * is_palindrome - function to check if a singly linked list is
 * a palindrome
 *
 * @head: pointer pointer to head node
 * Return: 1 if is a palindrome, 0 if it`s not
 *
 * Description: c function to check if a singley linked list is a palindrom
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *prev_node, *curr_node, *h;

	if (!(*head))
		return (1);

	/* step one: make a copy and reverse the copy */
	temp = h = *head;
	prev_node = temp;
	curr_node = temp->next;
	temp = temp->next;

	prev_node->next = NULL;

	while (temp)
	{
		temp = temp->next;
		curr_node->next = prev_node;
		prev_node = curr_node;
		curr_node = temp;
	}
	temp = prev_node;
	/* step two: compare the reverse list and the copy of the original list*/
	while (h)
	{
		if (h->n != temp->n)
			return (0);
		h = h->next;
		temp = temp->next;
	}
		
	return (1);
}
