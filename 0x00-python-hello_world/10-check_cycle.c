#include "lists.h"
#include <stdlib.h>

/*
 * check_cycle - Check if there is a cycle in a node list
 * @list: the list to start from
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *next;
	listint_t *temp;

	temp = list;

	while (list != NULL && (next = list->next) != NULL)
	{
		list = next;

		if (list == temp)
			return (1);
	}

	return (0);
}
