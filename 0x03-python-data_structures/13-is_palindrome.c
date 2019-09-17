#include "lists.h"
/**
 * is_palindrome - finds palindromism in a list
 * @head: pointer to the first node
 * Return: retunr 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	size_t list_le = list_len(*head);
	listint_t *temp = *head;
	size_t count = 0, iter = 0;
	int buffer[1024];

	if (head == NULL)
		return (0);

	if (list_le == 0 || list_le == 1)
	{
		return (1);
	}
	while (temp)
	{
		buffer[count] = temp->n;
		count++;
		temp = temp->next;
	}

	while (iter <= (list_le - 1))
	{
		if (buffer[iter] != buffer[list_le - 1])
			return (0);
		iter++;
		list_le--;
	}
	return (1);


}
/**
 * list_len - prints the number of elements of a list
 * @h: pointer to the list
 * Return: number of elements
 */
size_t list_len(const listint_t *h)
{
	size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
