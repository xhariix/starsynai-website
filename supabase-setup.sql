-- =============================================================
--  StarSyn AI — database setup
--  Paste this whole file into the Supabase SQL Editor and Run.
--  Safe to run more than once.
-- =============================================================
--  The site writes to four tables with the public anon key. That key is
--  visible in the page source by design, so every table below is
--  insert-only for the public and readable only by you in the dashboard.
--  Without these policies the anon key could read every enquiry you have
--  ever received.
-- =============================================================

-- ---------- enquiries from the contact form ----------
create table if not exists public.contacts (
  id          bigint generated always as identity primary key,
  first_name  text,
  last_name   text,
  email       text,
  phone       text,
  interest    text,
  message     text,
  created_at  timestamptz not null default now()
);

-- ---------- footer newsletter signups ----------
create table if not exists public.newsletter_subscribers (
  id          bigint generated always as identity primary key,
  email       text,
  source      text,
  created_at  timestamptz not null default now()
);

-- ---------- lightweight analytics ----------
create table if not exists public.page_visits (
  id          bigint generated always as identity primary key,
  url         text,
  referrer    text,
  user_agent  text,
  created_at  timestamptz not null default now()
);

create table if not exists public.visitors (
  id          bigint generated always as identity primary key,
  event       text,
  created_at  timestamptz not null default now()
);

-- ---------- lock them down ----------
alter table public.contacts               enable row level security;
alter table public.newsletter_subscribers enable row level security;
alter table public.page_visits            enable row level security;
alter table public.visitors               enable row level security;

-- The website may add rows. It may not read them back.
drop policy if exists "anon can insert" on public.contacts;
create policy "anon can insert" on public.contacts
  for insert to anon with check (true);

drop policy if exists "anon can insert" on public.newsletter_subscribers;
create policy "anon can insert" on public.newsletter_subscribers
  for insert to anon with check (true);

drop policy if exists "anon can insert" on public.page_visits;
create policy "anon can insert" on public.page_visits
  for insert to anon with check (true);

drop policy if exists "anon can insert" on public.visitors;
create policy "anon can insert" on public.visitors
  for insert to anon with check (true);

-- No select/update/delete policy is created on purpose. With RLS on and no
-- read policy, the anon key cannot read anything. You still see everything
-- in the Supabase Table Editor, which uses your own credentials.

-- ---------- handy for the dashboard ----------
create index if not exists contacts_created_at_idx
  on public.contacts (created_at desc);
create index if not exists newsletter_created_at_idx
  on public.newsletter_subscribers (created_at desc);
create index if not exists page_visits_created_at_idx
  on public.page_visits (created_at desc);
