import type { Locale } from '@/i18n/config';

import fr from '@/messages/fr.json';

export type Messages = typeof fr;

const allMessages: Record<Locale, Messages> = {
  fr,
};

export function getMessages(locale: Locale): Messages {
  return allMessages[locale] || allMessages.fr;
}
