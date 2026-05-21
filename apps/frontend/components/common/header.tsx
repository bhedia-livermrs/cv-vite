'use client';

import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { useTranslations } from '@/lib/i18n';

export function Header() {
  const { t } = useTranslations();

  return (
    <header className="border-b border-black bg-white shrink-0 sticky top-0 z-50">
      <div className="max-w-[1800px] mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-3 group">
          <Image
            src="/logo.svg"
            alt="CV Liver"
            width={32}
            height={32}
            className="w-8 h-8 group-hover:scale-105 transition-transform"
          />
          <span className="font-serif font-bold text-xl uppercase tracking-tight hidden sm:block">
            CV Liver
          </span>
        </Link>
        <div className="flex items-center gap-6">
          <Link
            href="/dashboard"
            className="text-sm font-mono font-bold uppercase hover:text-blue-700 transition-colors"
          >
            {t('nav.dashboard')}
          </Link>
          <Link
            href="/settings"
            className="text-sm font-mono font-bold uppercase hover:text-blue-700 transition-colors"
          >
            {t('nav.settings')}
          </Link>
        </div>
      </div>
    </header>
  );
}
