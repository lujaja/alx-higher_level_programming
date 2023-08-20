#include "lists.h"
/**
 * is_palindrome - function to check if a singly linked list is
 * a palindrome
 *
 * @head: pointer pointer to head node
 * Return: 1 if is a palindrome, 0 if it`s not
 *
 * Description: c function to check if a singley linked list is a palindrom
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *f, *s, *temp, *temp_node_size;

	int i = 0, size = 0;

	if (!(*head) || (*head)->next == NULL)
		return (1);
	s = temp_node_size = *head;
	size = node_len(*head);

	if (size % 2 == 0)
	{
		i++;

		while (i < (size / 2))
		{
			s = s->next;
			i++;
		}
		f = s->next;
	}
	else
	{
		while (i < ((size / 2) - 1))
		{
			s = s->next;
			i++;
		}
		f = s->next->next;
	}
	s->next = NULL;
	temp = reverse_listint(&f);
	while (temp)
	{
		if (temp->n != (*head)->n)
			return (0);
		temp = temp->next;
		*head = (*head)->next;
	}
	return (1);
}
