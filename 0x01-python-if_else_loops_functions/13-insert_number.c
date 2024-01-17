#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node: Insert a number into a sorted linked list
 * @head: the current head
 * @number: the number
 * Return: the node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	if (*head == NULL)
		return (NULL);

	current = *head;
	prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = current;
	}

	return (new);

}
