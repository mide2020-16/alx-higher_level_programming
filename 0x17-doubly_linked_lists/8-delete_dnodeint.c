#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes a node at a particular index
 * @head: The node to delete
 * @index: the index of the the node
 * Return: 1 on Success and -1 for Failure
*/
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current;

	if (head == NULL || index < 0)
		return -1;

	current = *head;

	if (current == NULL)
		return (-1);

	while (current != NULL)
		current = current->next;
	
	if (current->prev != NULL)
		current->prev->next = current->next;
	else
		*head = current->next;

	if (current->next != NULL)
		current->next->prev = current->prev;

	free_dlistint(current);
	return (1);
}
