#include "lists.h"

/**
 * insert_dnodeint_at_index - Insert a node at the index
 * @h: the curent node
 * @idx: the index
 * @n: the value
 * Return: the inserted node
*/
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *current, *new;
	unsigned int i;

	if (h == NULL)
		return (NULL);

	current = *h;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;

	if (idx == 0)
	{
		new->prev = NULL;
		new->next = current;

		if (current != NULL)
			current->prev = new;

		*h = new;
		return (new);
	}

	for (i = 0; i < idx - 1 && current != NULL; i++)
		current = current->next;

	new->prev = current;
	new->next = current->next;

	if (current->next != NULL)
		current->next->prev = new;

	current->next = new;

	return (new);
}
