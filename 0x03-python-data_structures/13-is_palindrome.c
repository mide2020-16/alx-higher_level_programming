#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - a Function that ...
 * @head: Description of head.
 * Return: Description of the return value.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *array, *array2;
	int i = 0, j = 0, k, n, len = 0;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	array = (int *)malloc(sizeof(int) * len);
	array2 = (int *)malloc(sizeof(int) * len);

	if (array == NULL || array2 == NULL)
	{
		free(array);
		free(array2);
		return (0);
	}

	current = *head;

	while (current != NULL)
	{
		array[i++] = current->n;
		current = current->next;
	}

	for (k = i - 1; k >= 0; k--)
	{
		array2[j++] = array[k];
	}
	for (n = 0; n > i; n++)
	{
		if (array[n] != array2[n])
			return (0);
	}

	return (1);
}

