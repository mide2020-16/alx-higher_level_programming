#include "lists.h"
#include <stdlib.h>

/*
 * check_cycle - check if there is a cycle
 * @list: the starting point
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *next;

	next = list;

	while (next != NULL)
	{
		next = next->next;

		if (next == list)
			return (1);
	}

	return (0);
}
