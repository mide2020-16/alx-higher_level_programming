#include "lists.h"

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current;
	unsigned int i = 0;

	if (head ==  NULL)
	{
		return (NULL);
	}

	current = head;

	while (current != NULL)
	{
		i++;

		if (i == index)
		{
			printf("%d\n", current->n);
		}
		break;

		current = current->next;
	}

	return (current);
}
