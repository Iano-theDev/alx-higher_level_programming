#include "lists.h"
#include <stddef.h>
#include <stdio.h>

listint_t *reverse_list(listint_t **head);

/**
* is_palindrome - checks if listint_t is a palinrome
* @head: pointer to the head of the list
* Return: 0 if it's not a palindrome, 1 if it is.
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev = reverse_list(head), *current = *head;

	if (*head == NULL)
		return (0);

	while (current != NULL && rev != NULL)
	{
		if (current->n == rev->n)
		{
			current = current->next;
			rev = rev->next;
		}
		else
			return (0);
	}
	return (1);
}

/**
* reverse_list - reverses a linked list
* @head: pointer to the head of listint_t list
* Return: pointer to the head of the reversed linked list
*/
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next;

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
