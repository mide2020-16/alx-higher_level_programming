#include "lists.h"

/**
 * free_dlistint - Free each node after its execution
 * @head: the current node
*/
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current, *next;

	current = head;

	while (current != NULL)
	{
		next = current->next;
		free(current);
		current = next;
	}

}
