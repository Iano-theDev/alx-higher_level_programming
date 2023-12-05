#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

listint_t *reverse_list(listint_t **head);
listint_t *copy_list(listint_t **head);

/**
* is_palindrome - checks if listint_t is a palinrome
* @head: pointer to the head of the list
* Return: 0 if it's not a palindrome, 1 if it is.
*/
int is_palindrome(listint_t **head)
{
	listint_t *head_copy = copy_list(head), *current = *head;
	listint_t *rev = reverse_list(&head_copy);

	if (*head == NULL)
		return (1);

	while (current != NULL && rev != NULL)
	{
		if (current->n == rev->n)
		{
			current = current->next;
			rev = rev->next;
		}
		else
		{
			free_listint(head_copy);
			return (0);
		}
	}
	free_listint(head_copy);
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
/**
* copy_list - returns a copy of a listint_t list
* @head: pointer to the head of a listint_t list
* Return: pointer to new listint_t list
*/
listint_t *copy_list(listint_t **head)
{
	listint_t *new, *ptr, *current = *head;

	if (*head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	ptr = new;

	while (current != NULL)
	{
		ptr->n = current->n;

		if (current->next != NULL)
		{
			ptr->next = malloc(sizeof(listint_t));

			if (ptr->next == NULL)
				return (NULL);
			ptr = ptr->next;
		}
		ptr->next = NULL;
		current = current->next;
	}
	return (new);
}
