#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: first node
 * Return: 0 if not pali, 1 if pali
 */
int is_palindrome(listint_t **head)
{
	listint_t *gettoend;
	listint_t *temp = *head;

	while (*head)
	{
		temp = temp->next;
		gettoend = temp;
	}

	while (*head)
	{
		if (temp->n == gettoend->n)
		{
			temp = temp->next;
			return (1);
		}
		else
			return (0);
	}
	return (0);
}
