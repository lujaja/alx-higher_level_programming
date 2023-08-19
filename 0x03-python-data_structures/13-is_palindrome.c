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
	listint_t *rev_node, *temp_node;
	
	if (!(*head) || !((*head)->next))
		return (1);

	temp_node = *head;
	rev_node = reverse_listint(&(*head));
	printf("------------\n");
	print_listint(*head);
	while (temp_node && rev_node)
	{
		if (temp_node->n > rev_node->n || temp_node->n < rev_node->n)
			return (0);
		rev_node = rev_node->next;
		temp_node = temp_node->next;
	}

	return (1);
}
