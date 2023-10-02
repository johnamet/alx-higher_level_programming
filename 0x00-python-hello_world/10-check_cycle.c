#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has cycle in it
 * @list: Pointer to check teh list
 *
 * Return: 0 if there is no cycle 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *step = list;
	listint_t *two_steps = list->next;

	while (step != NULL && two_steps != NULL)
	{
		if (step == two_steps)
			return (1);

		step = step->next;
		two_steps = two_steps->next;
	}

	return (0);
}
