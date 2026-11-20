
## Supabase login

`index.html` includes the supplied Supabase publishable client configuration and a login button/modal with sign-in, sign-up, password reset, session restore, and logout. Before publishing, confirm the Supabase project has the desired email confirmation, redirect URL, password policy, and Row Level Security policies enabled. Only publishable/anon client credentials belong in static HTML; never embed a service-role key.
