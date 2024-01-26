#include "lists.h"

/**
 * sum_dlistint - Sums up all the value in a node
 * @head: the starting point of summation
 * Return: the sum
*/
int sum_dlistint(dlistint_t *head)
{
        dlistint_t *current;
        int sum = 0;

        if (head == NULL)
                return (0);

        current = head;

        while (current != NULL)
        {
                sum += current->n;
                current = current->next;
        }

        return (sum);
}
