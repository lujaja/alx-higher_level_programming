#include "lists.h"
/**
 * insert_node - Function name
 *
 * @head: pointer pointer to head node
 * @number: number to insert in sorted list
 * Return: pointer to inserted node or null if it fails
 *
 * Description: function to insert a number into a sorted singly linked list
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr;

	new_node = (listint_t *) malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!(*head) || ((*head)->n) >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr = *head;

	while (curr->next != NULL && curr->next->n < new_node->n)
		curr = curr->next;

	new_node->next = curr->next;
	curr->next = new_node;
	
	return (new_node);
}
