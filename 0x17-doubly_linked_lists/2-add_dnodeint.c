#include "lists.h"

/**
 * add_dnodeint - adds a new node to a list at the beginning
 * @head: the current node
 * @n: the data to store
 * Return: the new node created
*/
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->prev = NULL;
	new->next = *head;

	if (*head != NULL)
		(*head)->prev = new;

	*head = new;

	return (new);
}
