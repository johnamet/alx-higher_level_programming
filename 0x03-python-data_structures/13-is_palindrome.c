#include "lists.h"

/**
 * reverse_listint - reverses the list
 * @head: Head of the node
 * Return: Reversed head
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - Checks whether a linked list is palindrome
 * @head: Start of the node
 *
 * Return: 0 is not a palindrome 1 is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed = NULL;
	listint_t *tmp = NULL;

	reversed = reverse_listint(head);
	tmp = reversed;

	while (*head != NULL && tmp != NULL)
	{
		if ((*head)->n != tmp->n)
		{
			free(reversed);
			return (0);
		}

		*head = (*head)->next;
		tmp = tmp->next;
	}

	free_listint(reversed);

	return (1);
}
