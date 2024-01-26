#include "lists.h"

size_t dlistint_len(const dlistint_t *h)
{
        const dlistint_t *current;
        size_t n = 0;

        current = h;

        while (current != NULL)
        {
                current = current->next;
                n++;
        }

        return (n);
}
