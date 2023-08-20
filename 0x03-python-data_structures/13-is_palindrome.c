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
/**
 * reverse_listint - function
 *
 * @head: pointer pinter to head node
 * Return: reversed listint or NULL if it fails
 *
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *curr_node, *prev_node, *next_node;

	curr_node = *head;
	prev_node = NULL;
	while (curr_node)
	{
		next_node = curr_node->next;
		curr_node->next = prev_node;
		prev_node = curr_node;
		curr_node = next_node;
	}
	*head = prev_node;
	return (*head);
}
/**
 * node_len - function
 * @h: pointer
 *
 * Return: number of node
 */
int node_len(const listint_t *h)
{
	int size = 0;

	while (h)
	{
		size++;
		h = h->next;
	}
	return (size);
}
