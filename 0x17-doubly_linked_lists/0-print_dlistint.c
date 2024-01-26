#include "lists.h"

/**
 * print_dlistint - Prints the Length of nodes in a list
 * and also prints it's data
 * 
 * @h: the head of the list
 * Return: the number of nodes present
*/
size_t print_dlistint(const dlistint_t *h)
{
	unsigned int n = 0;
	const dlistint_t *current;

	current = h;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}
