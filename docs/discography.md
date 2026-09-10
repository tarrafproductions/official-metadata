# TARRAF PRODUCTIONS — Official Discography Register

This document is the human-readable index of the canonical catalog of the 275 observed standalone single products published in this repository. The machine-readable source is [`releases/studio-singles.jsonld`](../releases/studio-singles.jsonld).

## Scope and status

- 275 reconstructed digital single release products published as canonical JSON-LD.
- 275 distinct single recording rows with valid ISRC identifiers and durations.
- 275 single releases with valid UPC identifiers.
- 59 additional single products reconciled from first-party DistroKid dashboard detail records.
- 275 standalone single products observed in total.

This is a **verified canonical register of the 275 standalone single products observed in the supplied first-party DistroKid catalog evidence**. The 59 products previously awaiting identifiers are documented in [`sources/distrokid-dashboard-observations-2026-09-04.json`](../sources/distrokid-dashboard-observations-2026-09-04.json) and are now reconciled into the JSON-LD release graph using their DistroKid release date, UPC, ISRC, duration, and explicit-content status. Missing or unsupported values continue to be omitted rather than inferred.

The live albums and their 64 ordered track positions are maintained in [`releases/live-trilogy.jsonld`](../releases/live-trilogy.jsonld) and [`releases/live-tracklists.jsonld`](../releases/live-tracklists.jsonld).

The [combined CSV](../exports/catalog.csv) and [JSON](../exports/catalog.json) exports join the singles and live trilogy by recording and release identity. The catalog has 338 unique ISRCs across 339 recording appearances: `Still Yours (LIVE)` appears on both its single and Vol. III. The [September 7 audit](catalog-audit-2026-09-07.md) documents the added durations, platform title aliases and outstanding source discrepancies.

The [23-screenshot follow-up](distrokid-reconciliation-2026-09-07.md) records five exact artist-credit corrections, Marina’s historical primary-artist attribution, and the APOCALYPSE deletion / AKFA EMPIRE reupload history. It confirms 23 UPCs and 22 visible ISRCs; More Lyubvi’s ISRC is outside its screenshot.

The existing `studio-singles.jsonld` filename is retained for integrations; its contents include studio, remix and live singles.

## Cover artwork

The repository preserves 282 supplied cover-art files (the original 279 plus three owner-supplied additions) in [`assets/covers/archive`](../assets/covers/archive), with source filenames and checksums in [`manifest.json`](../assets/covers/manifest.json). The archive uses source-order numbering. Verified release artwork is in [`assets/covers/by-release`](../assets/covers/by-release), where `cover-004.webp` corresponds to `SNG-004`, and so on.

<!-- BEGIN GENERATED ARTWORK STATUS -->
278 of 278 release products have a verified cover association (0 still need review). The [complete mapping](cover-mapping.md) includes singles and all three live albums; the [review record](cover-review-needed.md) documents owner confirmations and any unresolved artwork.
<!-- END GENERATED ARTWORK STATUS -->

Website integrations should use the explicit `coverPath` in [`release-map.json`](../assets/covers/release-map.json), joined by catalog ID, release identity or UPC. Unverified associations have a null path. The Artwork column below uses the same mapping.

GitHub provides version history and public provenance; it does not replace registrations with performing-rights organizations, mechanical-rights organizations, SoundExchange, distributors, ISRC/UPC agencies, or copyright authorities.

## Canonical standalone singles

| Catalog ID | Date | Release | Credited artist(s) | UPC | ISRC | Verification | Artwork |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SNG-001 | 2025-08-20 | SWINGS | Alik Tarraf | 199326055495 | QZZ792534259 | Source-normalized | [cover-001.webp](../assets/covers/by-release/cover-001.webp) |
| SNG-002 | 2025-08-21 | 13 YEARS | Alik Tarraf (feat. Marina Tarraf) | 199743998511 | QZZ792534485 | Source-normalized | [cover-002.webp](../assets/covers/by-release/cover-002.webp) |
| SNG-003 | 2025-08-21 | El balón siempre volará | Alik Tarraf | 199078124739 | QZZ792534415 | Source-normalized | [cover-003.webp](../assets/covers/by-release/cover-003.webp) |
| SNG-004 | 2025-08-21 | VVERH VNIZ | Alik Tarraf (feat. Marina Tarraf) | 199744998510 | QZZ792534453 | Source-normalized | [cover-004.webp](../assets/covers/by-release/cover-004.webp) |
| SNG-005 | 2025-08-21 | БЕЗЛЮДНАЯ ДОРОГА | Alik Tarraf | 199747028191 | QZZ792534449 | Source-normalized | [cover-005.webp](../assets/covers/by-release/cover-005.webp) |
| SNG-006 | 2025-08-21 | ДОБРО И ЗЛО | Alik Tarraf | 199743991291 | QZZ792534489 | Source-normalized | [cover-006.webp](../assets/covers/by-release/cover-006.webp) |
| SNG-007 | 2025-08-21 | Мяч Бифдяч | Alik Tarraf | 199078117762 | QZZ792534432 | Source-normalized | [cover-007.webp](../assets/covers/by-release/cover-007.webp) |
| SNG-008 | 2025-08-21 | НАДОЕЛО | Alik Tarraf | 199732985959 | QZZ792534538 | Source-normalized | [cover-008.webp](../assets/covers/by-release/cover-008.webp) |
| SNG-009 | 2025-08-21 | Назар | Alik Tarraf | 199078238818 | QZZ792534404 | Source-normalized | [cover-009.webp](../assets/covers/by-release/cover-009.webp) |
| SNG-010 | 2025-08-21 | РОДИТЕЛИ ВО МНЕ | Alik Tarraf | 199741999381 | QZZ792534493 | Source-normalized | [cover-010.webp](../assets/covers/by-release/cover-010.webp) |
| SNG-011 | 2025-08-21 | ЦЕ НАШ ВАЙБ | Alik Tarraf | 199078107558 | QZZ792534435 | Source-normalized | [cover-011.webp](../assets/covers/by-release/cover-011.webp) |
| SNG-012 | 2025-08-22 | Alik | Alik Tarraf | 199732966156 | QZZ792534567 | Source-normalized | [cover-012.webp](../assets/covers/by-release/cover-012.webp) |
| SNG-013 | 2025-08-22 | Boginya | Alik Tarraf (feat. Marina Tarraf) | 199732870927 | QZZ792549661 | Source-normalized | [cover-013.webp](../assets/covers/by-release/cover-013.webp) |
| SNG-014 | 2025-08-22 | OH MAMMA MIA | Alik Tarraf (feat. Marina Tarraf) | 199732907180 | QZZ792541089 | Source-normalized | [cover-014.webp](../assets/covers/by-release/cover-014.webp) |
| SNG-015 | 2025-08-22 | PROSTO | Marina Tarraf | 199732931703 | QZZ792534916 | Owner artist confirmation · 2026-09-07 | [cover-015.webp](../assets/covers/by-release/cover-015.webp) |
| SNG-016 | 2025-08-22 | Up and Down | Alik Tarraf (feat. Marina Tarraf) | 199732768187 | QZZ792573561 | Source-normalized | [cover-016.webp](../assets/covers/by-release/cover-016.webp) |
| SNG-017 | 2025-08-22 | Vyshel Alik Pogulyat | Marina Tarraf | 199732887307 | QZZ792546205 | Owner artist confirmation · 2026-09-07 | [cover-017.webp](../assets/covers/by-release/cover-017.webp) |
| SNG-018 | 2025-08-22 | ВОСТОЧНАЯ МАРИНА ((VIP MIX)) | Alik Tarraf | 199732883934 | QZZ792549391 | Source-normalized | [cover-018.webp](../assets/covers/by-release/cover-018.webp) |
| SNG-019 | 2025-08-22 | ВРЕМЯ | Alik Tarraf | 199732970443 | QZZ792534564 | Source-normalized | [cover-019.webp](../assets/covers/by-release/cover-019.webp) |
| SNG-020 | 2025-08-22 | Затмила Мы | Alik Tarraf | 199732840197 | QZZ792557117 | Source-normalized | [cover-020.webp](../assets/covers/by-release/cover-020.webp) |
| SNG-021 | 2025-08-22 | Зачем Зачем | Alik Tarraf | 199732834349 | QZZ792559514 | Source-normalized | [cover-021.webp](../assets/covers/by-release/cover-021.webp) |
| SNG-022 | 2025-08-22 | Качели (REMIX) | Alik Tarraf | 199732754234 | QZZ792578839 | Source-normalized | [cover-022.webp](../assets/covers/by-release/cover-022.webp) |
| SNG-023 | 2025-08-22 | Мы | Alik Tarraf | 199732876912 | QZZ792549429 | Source-normalized | [cover-023.webp](../assets/covers/by-release/cover-023.webp) |
| SNG-024 | 2025-08-22 | Ну Нина | Alik Tarraf | 199732891014 | QZZ792546059 | Source-normalized | [cover-024.webp](../assets/covers/by-release/cover-024.webp) |
| SNG-025 | 2025-08-22 | СЛОЖНО | Alik Tarraf | 199732962493 | QZZ792534569 | Source-normalized | [cover-025.webp](../assets/covers/by-release/cover-025.webp) |
| SNG-026 | 2025-08-22 | Ты Я Не Мы | Alik Tarraf | 199732794551 | QZZ792568528 | Source-normalized | [cover-026.webp](../assets/covers/by-release/cover-026.webp) |
| SNG-027 | 2025-08-22 | ملاكي و شيطاني | Alik Tarraf | 199732756191 | QZZ792576554 | Source-normalized | [cover-027.webp](../assets/covers/by-release/cover-027.webp) |
| SNG-028 | 2025-08-23 | PROSTO [Remix] | Alik Tarraf (feat. Marina Tarraf) | 199732478543 | QZZ7K2583227 | Source-normalized | [cover-028.webp](../assets/covers/by-release/cover-028.webp) |
| SNG-029 | 2025-08-23 | TARRAF STORY | Alik Tarraf | 199732477690 | QZZ7K2531050 | Source-normalized | [cover-029.webp](../assets/covers/by-release/cover-029.webp) |
| SNG-030 | 2025-08-24 | CHOOSE YOU | Alik Tarraf | 199732435249 | QZZ7K2539567 | Source-normalized | [cover-030.webp](../assets/covers/by-release/cover-030.webp) |
| SNG-031 | 2025-08-24 | NOISY SILENCE | Alik Tarraf | 199732298424 | QZZ7K2569335 | Source-normalized | [cover-031.webp](../assets/covers/by-release/cover-031.webp) |
| SNG-032 | 2025-08-24 | ШУМНАЯ ТИШИНА | Alik Tarraf | 199732340871 | QZZ7K2560887 | Source-normalized | [cover-032.webp](../assets/covers/by-release/cover-032.webp) |
| SNG-033 | 2025-08-25 | EAGLES NOT CROWS | Alik Tarraf | 199732029332 | QZZ7L2526027 | DistroKid screenshot · 2026-09-07 | [cover-033.webp](../assets/covers/by-release/cover-033.webp) |
| SNG-034 | 2025-08-25 | Качели (EMO Version) | Alik Tarraf | 199326044208 | QZZ792534374 | Source-normalized | [cover-034.webp](../assets/covers/by-release/cover-034.webp) |
| SNG-035 | 2025-08-26 | GOOD AND EVIL | Alik Tarraf | 199733796899 | QZZ7L2573240 | Source-normalized | [cover-035.webp](../assets/covers/by-release/cover-035.webp) |
| SNG-036 | 2025-08-26 | ГІМН УКРАЇНИ | Alik Tarraf | 199733968067 | QZZ7L2537421 | Source-normalized | [cover-036.webp](../assets/covers/by-release/cover-036.webp) |
| SNG-037 | 2025-08-27 | Why Why | Alik Tarraf | 199733643162 | QZZ7M2502769 | Source-normalized | [cover-037.webp](../assets/covers/by-release/cover-037.webp) |
| SNG-038 | 2025-08-29 | PARADOX | Alik Tarraf | 199733143686 | QZZ7N2505349 | Source-normalized | [cover-038.webp](../assets/covers/by-release/cover-038.webp) |
| SNG-039 | 2025-08-29 | Не Умоляй | Alik Tarraf | 199733158727 | QZZ7N2502093 | Source-normalized | [cover-039.webp](../assets/covers/by-release/cover-039.webp) |
| SNG-040 | 2025-09-01 | FORGET ME | Alik Tarraf | 199734201866 | QZZ7Q2500446 | DistroKid screenshot · 2026-09-07 | [cover-040.webp](../assets/covers/by-release/cover-040.webp) |
| SNG-041 | 2025-09-01 | НОЧЬ ОЖИВАЕТ | Alik Tarraf | 199734180055 | QZZ7Q2504670 | Source-normalized | [cover-041.webp](../assets/covers/by-release/cover-041.webp) |
| SNG-042 | 2025-09-02 | Воздушный Шар | Alik Tarraf | 199735951869 | QZZ7Q2550781 | Source-normalized | [cover-042.webp](../assets/covers/by-release/cover-042.webp) |
| SNG-043 | 2025-09-03 | RISING BALLOON | Alik Tarraf | 199735912389 | QZZ7Q2558452 | Source-normalized | [cover-043.webp](../assets/covers/by-release/cover-043.webp) |
| SNG-044 | 2025-09-05 | День Birthday | Alik Tarraf | 199735153539 | QZZ7S2512624 | Source-normalized | [cover-044.webp](../assets/covers/by-release/cover-044.webp) |
| SNG-045 | 2025-09-06 | Я НАРЦИСС | Alik Tarraf | 199735081801 | QZZ7S2525590 | Source-normalized | [cover-045.webp](../assets/covers/by-release/cover-045.webp) |
| SNG-046 | 2025-09-09 | AKFA EMPIRE | Alik Tarraf | 199736298130 | QZZ7T2562881 | DistroKid screenshot · 2026-09-07 | [cover-046.webp](../assets/covers/by-release/cover-046.webp) |
| SNG-047 | 2025-09-09 | КОНЕЦ СВЕТА | Alik Tarraf | 199736264265 | QZZ7T2578083 | Source-normalized | [cover-047.webp](../assets/covers/by-release/cover-047.webp) |
| SNG-048 | 2025-09-10 | GODDESS | Alik Tarraf Marina Tarraf | 199737907826 | QZZ7U2554210 | DistroKid screenshot · 2026-09-07 | [cover-048.webp](../assets/covers/by-release/cover-048.webp) |
| SNG-049 | 2025-09-11 | PARADISE | Alik Tarraf | 199737886343 | QZZ7U2557695 | Source-normalized | [cover-049.webp](../assets/covers/by-release/cover-049.webp) |
| SNG-050 | 2025-09-12 | Semya v Serdtse | Alik Tarraf (feat. Aliana Tarraf) | 199737495767 | QZZ7V2541692 | Source-normalized | [cover-050.webp](../assets/covers/by-release/cover-050.webp) |
| SNG-051 | 2025-09-12 | Shtorm i Lyubov | Marina Tarraf | 199737612591 | QZZ7V2520401 | DistroKid screenshot · 2026-09-07 | [cover-051.webp](../assets/covers/by-release/cover-051.webp) |
| SNG-052 | 2025-09-12 | Sila Lyubvi | Alik Tarraf | 199737598277 | QZZ7V2523510 | DistroKid screenshot · 2026-09-07 | [cover-052.webp](../assets/covers/by-release/cover-052.webp) |
| SNG-053 | 2025-09-13 | ASH and NEON | Alik Tarraf | 199737136721 | QZZ7W2511469 | Source-normalized | [cover-053.webp](../assets/covers/by-release/cover-053.webp) |
| SNG-054 | 2025-09-14 | More Lyubvi | Alik Tarraf (feat. Marina Tarraf) | 199737115979 | QZZ7W2515106 | DistroKid UPC/title · ISRC retained | [cover-054.webp](../assets/covers/by-release/cover-054.webp) |
| SNG-055 | 2025-09-14 | Фальшивая Любовь | Alik Tarraf | 199738970133 | QZZ7W2545487 | Source-normalized | [cover-055.webp](../assets/covers/by-release/cover-055.webp) |
| SNG-056 | 2025-09-15 | Sister | Alik Tarraf | 199738677605 | QZZ7X2503248 | Source-normalized | [cover-056.webp](../assets/covers/by-release/cover-056.webp) |
| SNG-057 | 2025-09-15 | Брат | Alik Tarraf | 199738685365 | QZZ7X2501327 | Source-normalized | [cover-057.webp](../assets/covers/by-release/cover-057.webp) |
| SNG-058 | 2025-09-17 | Brother | Alik Tarraf | 199738216408 | QZZ7X2594221 | Source-normalized | [cover-058.webp](../assets/covers/by-release/cover-058.webp) |
| SNG-059 | 2025-09-19 | New World | Alik Tarraf Marina Tarraf | 199739691075 | QT3EY2513941 | DistroKid screenshot · 2026-09-07 | [cover-059.webp](../assets/covers/by-release/cover-059.webp) |
| SNG-060 | 2025-09-19 | STOP НАРКОТИК | Alik Tarraf | 199739862048 | QT3EX2572244 | Source-normalized | [cover-060.webp](../assets/covers/by-release/cover-060.webp) |
| SNG-061 | 2025-09-20 | ARRIBA Y ABAJO | Alik Tarraf | 199739554028 | QT3EY2542532 | Source-normalized | [cover-061.webp](../assets/covers/by-release/cover-061.webp) |
| SNG-062 | 2025-09-20 | Бусинка | Alik Tarraf | 199739520566 | QT3EY2549935 | Source-normalized | [cover-062.webp](../assets/covers/by-release/cover-062.webp) |
| SNG-063 | 2025-09-21 | IBIZA FESTIVAL (soundtrack) | Alik Tarraf | 199739237730 | QT3EZ2511468 | Source-normalized | [cover-063.webp](../assets/covers/by-release/cover-063.webp) |
| SNG-064 | 2025-09-21 | МОЛОДОСТЬ | Alik Tarraf | 199739238287 | QT3EZ2508067 | Source-normalized | [cover-064.webp](../assets/covers/by-release/cover-064.webp) |
| SNG-065 | 2025-09-22 | HELA | Alik Tarraf | 199739106517 | QT3EZ2529962 | DistroKid screenshot · 2026-09-07 | [cover-065.webp](../assets/covers/by-release/cover-065.webp) |
| SNG-066 | 2025-09-23 | ДЕТСТВО | Alik Tarraf | 199740856524 | QT3EZ2585905 | Source-normalized | [cover-066.webp](../assets/covers/by-release/cover-066.webp) |
| SNG-067 | 2025-09-23 | УХУ ЕЛ? | Alik Tarraf | 199740652089 | QT3F22532818 | Source-normalized | [cover-067.webp](../assets/covers/by-release/cover-067.webp) |
| SNG-068 | 2025-09-25 | ДОБРО И ЗЛО ((VIP REMIX Version)) | Alik Tarraf | 199740131089 | QT3F32547780 | Source-normalized | [cover-068.webp](../assets/covers/by-release/cover-068.webp) |
| SNG-069 | 2025-09-25 | ملاك و شيطان | Alik Tarraf | 199740139177 | QT3F32544991 | Source-normalized | [cover-069.webp](../assets/covers/by-release/cover-069.webp) |
| SNG-070 | 2025-09-26 | БЛИЗНЕЦЫ В ОГНЕ | Alik Tarraf | 199740087768 | QT3F32554998 | Source-normalized | [cover-070.webp](../assets/covers/by-release/cover-070.webp) |
| SNG-071 | 2025-09-27 | HELAH | Alik Tarraf | 199741624603 | QT3F42551251 | Source-normalized | [cover-071.webp](../assets/covers/by-release/cover-071.webp) |
| SNG-072 | 2025-09-28 | DESTINATION (soundtrack) | Alik Tarraf | 199741391727 | QT3F42594065 | Source-normalized | [cover-072.webp](../assets/covers/by-release/cover-072.webp) |
| SNG-073 | 2025-09-28 | LOST (soundtrack) | Alik Tarraf | 199741393233 | QT3F42592202 | Source-normalized | [cover-073.webp](../assets/covers/by-release/cover-073.webp) |
| SNG-074 | 2025-09-28 | Ай Одесса | Alik Tarraf | 199741332973 | QT3F52503218 | Source-normalized | [cover-074.webp](../assets/covers/by-release/cover-074.webp) |
| SNG-075 | 2025-09-29 | Гимн Одессы | Alik Tarraf | 199741244023 | QT3F52518015 | Source-normalized | [cover-075.webp](../assets/covers/by-release/cover-075.webp) |
| SNG-076 | 2025-09-30 | HELLA | Alik Tarraf | 199741008069 | QT3F52572933 | Source-normalized | [cover-076.webp](../assets/covers/by-release/cover-076.webp) |
| SNG-077 | 2025-09-30 | ГОРЬКО | Alik Tarraf | 199741006461 | QT3F52575403 | Source-normalized | [cover-077.webp](../assets/covers/by-release/cover-077.webp) |
| SNG-078 | 2025-09-30 | Смысл Жизни | Alik Tarraf | 199742899222 | QT3F52596011 | Source-normalized | [cover-078.webp](../assets/covers/by-release/cover-078.webp) |
| SNG-079 | 2025-10-01 | ЛЕТИ | Alik Tarraf | 199742726863 | QT3F62535970 | Source-normalized | [cover-079.webp](../assets/covers/by-release/cover-079.webp) |
| SNG-080 | 2025-10-02 | ABU DHABI NIGHTS | Alik Tarraf | 199742334662 | QT3F72520533 | Source-normalized | [cover-080.webp](../assets/covers/by-release/cover-080.webp) |
| SNG-081 | 2025-10-02 | ВЛАСТЬ | Alik Tarraf | 199742433303 | QT3F72503137 | Source-normalized | [cover-081.webp](../assets/covers/by-release/cover-081.webp) |
| SNG-082 | 2025-10-02 | Сум за Батьківщиною | Alik Tarraf | 199742427463 | QT3F72503317 | Source-normalized | [cover-082.webp](../assets/covers/by-release/cover-082.webp) |
| SNG-083 | 2025-10-02 | Это Мои Чувства | Alik Tarraf | 199742429412 | QT3F72503236 | Source-normalized | [cover-083.webp](../assets/covers/by-release/cover-083.webp) |
| SNG-084 | 2025-10-03 | Предназначение | Alik Tarraf | 199742114868 | QT3F72570597 | Source-normalized | [cover-084.webp](../assets/covers/by-release/cover-084.webp) |
| SNG-085 | 2025-10-03 | Я ПРОЩАЮ | Alik Tarraf | 199742121392 | QT3F72567496 | Source-normalized | [cover-085.webp](../assets/covers/by-release/cover-085.webp) |
| SNG-086 | 2025-10-03 | Я Это Ты | Alik Tarraf | 199742118866 | QT3F72570593 | Source-normalized | [cover-086.webp](../assets/covers/by-release/cover-086.webp) |
| SNG-087 | 2025-10-04 | DistroKid (soundtrack) | Alik Tarraf | 199743787337 | QT3F82541888 | Source-normalized | [cover-087.webp](../assets/covers/by-release/cover-087.webp) |
| SNG-088 | 2025-10-04 | Dubai Lights | Alik Tarraf | 199743751253 | QT3F82547782 | Source-normalized | [cover-088.webp](../assets/covers/by-release/cover-088.webp) |
| SNG-089 | 2025-10-05 | Sanctum Fire | Alik Tarraf | 199743450811 | QT3F92507283 | Source-normalized | [cover-089.webp](../assets/covers/by-release/cover-089.webp) |
| SNG-090 | 2025-10-05 | ЗСУ | Alik Tarraf | 199743546187 | QT3F82587252 | Source-normalized | [cover-090.webp](../assets/covers/by-release/cover-090.webp) |
| SNG-091 | 2025-10-05 | КИЇВ | Alik Tarraf | 199743549454 | QT3F82583937 | Source-normalized | [cover-091.webp](../assets/covers/by-release/cover-091.webp) |
| SNG-092 | 2025-10-05 | ПРОЩАЙ | Alik Tarraf | 199743524048 | QT3F82590514 | Source-normalized | [cover-092.webp](../assets/covers/by-release/cover-092.webp) |
| SNG-093 | 2025-10-05 | ТЕНИ | Alik Tarraf | 199743452464 | QT3F92505012 | Source-normalized | [cover-093.webp](../assets/covers/by-release/cover-093.webp) |
| SNG-094 | 2025-10-06 | POSSESSED | Marina Tarraf | 199743290448 | QT3F92537714 | DistroKid screenshot · 2026-09-07 | [cover-094.webp](../assets/covers/by-release/cover-094.webp) |
| SNG-095 | 2025-10-06 | Запретный Вкус | Alik Tarraf | 199743292206 | QT3F92535289 | Source-normalized | [cover-095.webp](../assets/covers/by-release/cover-095.webp) |
| SNG-096 | 2025-10-07 | Instagram (soundtrack) | Alik Tarraf | 199744958323 | QT3FA2508029 | Source-normalized | [cover-096.webp](../assets/covers/by-release/cover-096.webp) |
| SNG-097 | 2025-10-07 | Пенсия Кайф | Alik Tarraf | 199744915647 | QT3FA2517875 | Source-normalized | [cover-097.webp](../assets/covers/by-release/cover-097.webp) |
| SNG-098 | 2025-10-09 | COSMOS LIFE СЕРИЯ 1 - ПЛАНЕТА БЕЗ ЛЮДЕЙ | Alik Tarraf | 199744399263 | QT3FB2522842 | Source-normalized | [cover-098.webp](../assets/covers/by-release/cover-098.webp) |
| SNG-099 | 2025-10-10 | COSMOS LIFE СЕРИЯ 2 - АДАМ И ЕВА | Alik Tarraf | 199744168395 | QT3FB2572738 | Source-normalized | [cover-099.webp](../assets/covers/by-release/cover-099.webp) |
| SNG-100 | 2025-10-11 | COSMOS LIFE СЕРИЯ З - «РАЗРУШЕНИЕ» | Alik Tarraf | 199745847077 | QT3FC2537576 | Source-normalized | [cover-100.webp](../assets/covers/by-release/cover-100.webp) |
| SNG-101 | 2025-10-12 | COSMOS LIFE СЕРИЯ 4 - «COSMOS LIFE» | Alik Tarraf | 199745608012 | QT3FC2583008 | Source-normalized | [cover-101.webp](../assets/covers/by-release/cover-101.webp) |
| SNG-102 | 2025-10-12 | Мама | Alik Tarraf | 199745489772 | QT3FD2506128 | Source-normalized | [cover-102.webp](../assets/covers/by-release/cover-102.webp) |
| SNG-103 | 2025-10-13 | DREAM OF LIGHT | Alik Tarraf | 199745241905 | QT3FD2561541 | Source-normalized | [cover-103.webp](../assets/covers/by-release/cover-103.webp) |
| SNG-104 | 2025-10-14 | Между Орбит | Alik Tarraf | 199745016800 | QT3FE2509181 | Source-normalized | [cover-104.webp](../assets/covers/by-release/cover-104.webp) |
| SNG-105 | 2025-10-17 | Anima Obscura (Dark Ritual Song) | Alik Tarraf | 199746102007 | QT3FG2507072 | DistroKid screenshot · 2026-09-07 | [cover-105.webp](../assets/covers/by-release/cover-105.webp) |
| SNG-106 | 2025-10-17 | HELLO | Alik Tarraf | 199746331070 | QT3FF2557854 | Source-normalized | [cover-106.webp](../assets/covers/by-release/cover-106.webp) |
| SNG-107 | 2025-10-19 | БУМЕРАНГ | Alik Tarraf | 199747546978 | QT3FH2514472 | Source-normalized | [cover-107.webp](../assets/covers/by-release/cover-107.webp) |
| SNG-108 | 2025-10-22 | Meaning of Life | Alik Tarraf | 199748808495 | QT6E52575346 | DistroKid screenshot · 2026-09-07 | [cover-108.webp](../assets/covers/by-release/cover-108.webp) |
| SNG-109 | 2025-10-22 | VEVO | Alik Tarraf | 199748950453 | QT6E52548061 | Source-normalized | [cover-109.webp](../assets/covers/by-release/cover-109.webp) |
| SNG-110 | 2025-10-23 | BANINA BANINA YALLA TARRAF | Alik Tarraf, Marina Tarraf | 199748545277 | QT6E62524228 | DistroKid screenshot · 2026-09-07 | [cover-110.webp](../assets/covers/by-release/cover-110.webp) |
| SNG-111 | 2025-10-23 | ПІСНЯ КРАКЕНА — “ВІТО І ЮТА” | Alik Tarraf | 199748424800 | QT6E62558415 | Source-normalized | [cover-111.webp](../assets/covers/by-release/cover-111.webp) |
| SNG-112 | 2025-10-24 | ВРЕМЯ НЕ ПРОЩАЕТ | Alik Tarraf | 199748201050 | QT6E72510455 | Source-normalized | [cover-112.webp](../assets/covers/by-release/cover-112.webp) |
| SNG-113 | 2025-10-25 | КРАКЕН — ВІТО ШТОРМ ((VIP MIX)) | Alik Tarraf | 199749938153 | QT6E82567761 | Source-normalized | [cover-113.webp](../assets/covers/by-release/cover-113.webp) |
| SNG-114 | 2025-10-25 | ПІСНЯ КРАКЕН — ВІТО ШТОРМ | Alik Tarraf | 199748119218 | QT6E72527928 | Source-normalized | [cover-114.webp](../assets/covers/by-release/cover-114.webp) |
| SNG-115 | 2025-10-26 | Где Кончается Человек | Alik Tarraf | 199749709517 | QT6E82504500 | Source-normalized | [cover-115.webp](../assets/covers/by-release/cover-115.webp) |
| SNG-116 | 2025-10-26 | НЕ ГОНИ ФУФЛО | Alik Tarraf | 199749849954 | QT6E72580731 | Source-normalized | [cover-116.webp](../assets/covers/by-release/cover-116.webp) |
| SNG-117 | 2025-10-27 | The Other Side | Alik Tarraf | 199749343308 | QT6E82591324 | Source-normalized | [cover-117.webp](../assets/covers/by-release/cover-117.webp) |
| SNG-118 | 2025-10-27 | ПОЛИСАЙ | Alik Tarraf | 199749543050 | QT6E82542002 | Source-normalized | [cover-118.webp](../assets/covers/by-release/cover-118.webp) |
| SNG-119 | 2025-10-28 | NORA | Alik Tarraf (feat. Marina Tarraf) | 199749050473 | QT6E92567897 | Source-normalized | [cover-119.webp](../assets/covers/by-release/cover-119.webp) |
| SNG-120 | 2025-10-29 | ПАМЯТЬ | Alik Tarraf | 199750780994 | QT6EA2526339 | Source-normalized | [cover-120.webp](../assets/covers/by-release/cover-120.webp) |
| SNG-121 | 2025-10-30 | БРАТ ОНА БЕРЕМЕННА | Alik Tarraf | 199750667622 | QT6EA2554382 | Source-normalized | [cover-121.webp](../assets/covers/by-release/cover-121.webp) |
| SNG-122 | 2025-10-30 | Він Малює Світ | Alik Tarraf | 199750455298 | QT6EB2506047 | Source-normalized | [cover-122.webp](../assets/covers/by-release/cover-122.webp) |
| SNG-123 | 2025-11-01 | HALLOWEEN | Alik Tarraf | 199750038354 | QT6EB2599080 | Source-normalized | [cover-123.webp](../assets/covers/by-release/cover-123.webp) |
| SNG-124 | 2025-11-01 | Братва Не Спит | Alik Tarraf | 199750068924 | QT6EB2592278 | Source-normalized | [cover-124.webp](../assets/covers/by-release/cover-124.webp) |
| SNG-125 | 2025-11-02 | Ad Vinculum | Alik Tarraf | 199751799032 | QT6EC2548482 | Source-normalized | [cover-125.webp](../assets/covers/by-release/cover-125.webp) |
| SNG-126 | 2025-11-03 | СЕРДЦЕЕДКА | Alik Tarraf | 199751486697 | QT6ED2520205 | Source-normalized | [cover-126.webp](../assets/covers/by-release/cover-126.webp) |
| SNG-127 | 2025-11-03 | Сухая Вода | Alik Tarraf | 199751500447 | QT6ED2514535 | Source-normalized | [cover-127.webp](../assets/covers/by-release/cover-127.webp) |
| SNG-128 | 2025-11-04 | ПАПА | Alik Tarraf | 199940998956 | QT6EE2520051 | Source-normalized | [cover-128.webp](../assets/covers/by-release/cover-128.webp) |
| SNG-129 | 2025-11-05 | Да … Нет | Alik Tarraf | 199953996604 | QT6EE2580457 | Source-normalized | [cover-129.webp](../assets/covers/by-release/cover-129.webp) |
| SNG-130 | 2025-11-06 | UKRAINE | Alik Tarraf (feat. Marina Tarraf) | 199956747098 | QT6EF2541785 | Source-normalized | [cover-130.webp](../assets/covers/by-release/cover-130.webp) |
| SNG-131 | 2025-11-06 | Совесть | Alik Tarraf | 199956854468 | QT6EF2516843 | Source-normalized | [cover-131.webp](../assets/covers/by-release/cover-131.webp) |
| SNG-132 | 2025-11-07 | HE PAINTS THE WORLD | Alik Tarraf | 199956329850 | QT6EG2530117 | Source-normalized | [cover-132.webp](../assets/covers/by-release/cover-132.webp) |
| SNG-133 | 2025-11-09 | ПОЛНЫЙ АВТОБУС БУРАТИН | Alik Tarraf | 199955872593 | QT6ET2522351 | Source-normalized | [cover-133.webp](../assets/covers/by-release/cover-133.webp) |
| SNG-134 | 2025-11-10 | CODE OF SILENCE | Alik Tarraf | 199955473660 | QT6EU2504270 | Source-normalized | [cover-134.webp](../assets/covers/by-release/cover-134.webp) |
| SNG-135 | 2025-11-10 | КОД ТИШІ | Alik Tarraf | 199955682536 | QT6ET2559362 | Source-normalized | [cover-135.webp](../assets/covers/by-release/cover-135.webp) |
| SNG-136 | 2025-11-11 | KPOB I BIPA / BLOOD AND FAITH | Alik Tarraf | 199955214348 | QT6EU2556523 | Source-normalized | [cover-136.webp](../assets/covers/by-release/cover-136.webp) |
| SNG-137 | 2025-11-12 | BOOMERANG | Alik Tarraf | 199954873553 | QT6EV2526848 | Source-normalized | [cover-137.webp](../assets/covers/by-release/cover-137.webp) |
| SNG-138 | 2025-11-13 | THE CURE | Alik Tarraf | 199954510489 | QT6EW2510425 | Source-normalized | [cover-138.webp](../assets/covers/by-release/cover-138.webp) |
| SNG-139 | 2025-11-15 | RELEASE ME | Alik Tarraf | 199953870973 | QT6EX2543724 | Source-normalized | [cover-139.webp](../assets/covers/by-release/cover-139.webp) |
| SNG-140 | 2025-11-16 | Матрица Лжи (Matrix of lies) | Alik Tarraf | 199953749859 | QT6EX2564595 | Source-normalized | [cover-140.webp](../assets/covers/by-release/cover-140.webp) |
| SNG-141 | 2025-11-17 | ANIMALS | Alik Tarraf | 199953326517 | QT6EY2550384 | Source-normalized | [cover-141.webp](../assets/covers/by-release/cover-141.webp) |
| SNG-142 | 2025-11-17 | Храм Любви | Alik Tarraf | 199953371548 | QT6EY2542949 | Source-normalized | [cover-142.webp](../assets/covers/by-release/cover-142.webp) |
| SNG-143 | 2025-11-18 | Не Стыдно Падать | Alik Tarraf | 199952937097 | QT6EZ2529225 | Source-normalized | [cover-143.webp](../assets/covers/by-release/cover-143.webp) |
| SNG-144 | 2025-11-18 | Это ты Это я | Alik Tarraf | 199953125486 | QT6EY2596195 | Source-normalized | [cover-144.webp](../assets/covers/by-release/cover-144.webp) |
| SNG-145 | 2025-11-21 | Свет во мне | Alik Tarraf | 199951952558 | QT6F32506966 | Source-normalized | [cover-145.webp](../assets/covers/by-release/cover-145.webp) |
| SNG-146 | 2025-11-22 | Колючий, но родной | Alik Tarraf | 199951687337 | QT6F32560639 | Source-normalized | [cover-146.webp](../assets/covers/by-release/cover-146.webp) |
| SNG-147 | 2025-11-23 | Spotify (soundtrack) | Alik Tarraf | 199951307655 | QT6F52561642 | Source-normalized | [cover-147.webp](../assets/covers/by-release/cover-147.webp) |
| SNG-148 | 2025-11-23 | WORDS | Marina Tarraf | 199951361480 | QT6F42534566 | Source-normalized | [cover-148.webp](../assets/covers/by-release/cover-148.webp) |
| SNG-149 | 2025-11-24 | Слова | Marina Tarraf | 199949999626 | QT6F52509695 | Source-normalized | [cover-149.webp](../assets/covers/by-release/cover-149.webp) |
| SNG-150 | 2025-11-27 | ПРАВДА | Alik Tarraf | 199949067820 | QT6F72520888 | Source-normalized | [cover-150.webp](../assets/covers/by-release/cover-150.webp) |
| SNG-151 | 2025-11-28 | Monsters | Alik Tarraf (feat. Marina Tarraf) | 199952305674 | QT6F22539752 | Source-normalized | [cover-151.webp](../assets/covers/by-release/cover-151.webp) |
| SNG-152 | 2025-11-28 | ГІМН ЛЮБОВІ | Marina Tarraf | 199948759245 | QT6F72590802 | Source-normalized | [cover-152.webp](../assets/covers/by-release/cover-152.webp) |
| SNG-153 | 2025-11-29 | После Жизни | Alik Tarraf | 199948375773 | QT6F82569652 | Source-normalized | [cover-153.webp](../assets/covers/by-release/cover-153.webp) |
| SNG-154 | 2025-12-03 | Жизнь это Ринг | Alik Tarraf | 199946818388 | QT6FE2539776 | Source-normalized | [cover-154.webp](../assets/covers/by-release/cover-154.webp) |
| SNG-155 | 2025-12-04 | NO LIMIT ANIMAL MODE | Marina Tarraf | 199946783778 | QT6FE2548157 | Source-normalized | [cover-155.webp](../assets/covers/by-release/cover-155.webp) |
| SNG-156 | 2025-12-04 | А что если - это Сны? | Alik Tarraf | 199946637958 | QT6FE2583599 | Source-normalized | [cover-156.webp](../assets/covers/by-release/cover-156.webp) |
| SNG-157 | 2025-12-04 | ЛЮБОВЬ РЕЗНЯ | Alik Tarraf | 199946769482 | QT6FE2551286 | Source-normalized | [cover-157.webp](../assets/covers/by-release/cover-157.webp) |
| SNG-158 | 2025-12-05 | КАЧЕЛІ ((UA Version)) | Alik Tarraf | 199946180348 | QT6FF2584414 | Source-normalized | [cover-158.webp](../assets/covers/by-release/cover-158.webp) |
| SNG-159 | 2025-12-07 | Хочу Люблю Живу | Alik Tarraf | 199945630929 | QT6FH2505815 | Source-normalized | [cover-159.webp](../assets/covers/by-release/cover-159.webp) |
| SNG-160 | 2025-12-12 | EISENHERZ | Alik Tarraf | 199943938454 | QT6FL2567189 | Source-normalized | [cover-160.webp](../assets/covers/by-release/cover-160.webp) |
| SNG-161 | 2025-12-14 | HAPPY NEW YEAR WORLD | Alik Tarraf | 199943304181 | QT6FP2505649 | Source-normalized | [cover-161.webp](../assets/covers/by-release/cover-161.webp) |
| SNG-162 | 2025-12-14 | Ty Angel ya Demon | Alik Tarraf | 199943304211 | QT6FP2502129 | DistroKid screenshot · 2026-09-07 | [cover-162.webp](../assets/covers/by-release/cover-162.webp) |
| SNG-163 | 2025-12-15 | ДУША | Alik Tarraf | 199947581687 | QT6F92592333 | Source-normalized | [cover-163.webp](../assets/covers/by-release/cover-163.webp) |
| SNG-164 | 2025-12-16 | REBORN IN FIRE | Alik Tarraf | 199952858736 | QT6EZ2542620 | Source-normalized | [cover-164.webp](../assets/covers/by-release/cover-164.webp) |
| SNG-165 | 2025-12-19 | Я Свет Он Тень | Marina Tarraf | 199946812768 | QT6FE2543628 | Source-normalized | [cover-165.webp](../assets/covers/by-release/cover-165.webp) |
| SNG-166 | 2025-12-22 | AMERICAN DREAMS | Alik Tarraf | 199940314213 | QT6G52547940 | Source-normalized | [cover-166.webp](../assets/covers/by-release/cover-166.webp) |
| SNG-167 | 2025-12-23 | ЦЫГАНСКАЯ ДУША | Alik Tarraf | 199939868369 | QT6G62556719 | Source-normalized | [cover-167.webp](../assets/covers/by-release/cover-167.webp) |
| SNG-168 | 2025-12-24 | НИКТО КРОМЕ НАС | Alik Tarraf | 199939527679 | QT6G72538692 | DistroKid screenshot · 2026-09-07 | [cover-168.webp](../assets/covers/by-release/cover-168.webp) |
| SNG-169 | 2025-12-25 | КУПИ БИЛЕТ | Alik Tarraf | 199939309817 | QT6G72585854 | Source-normalized | [cover-169.webp](../assets/covers/by-release/cover-169.webp) |
| SNG-170 | 2025-12-29 | STILL YOURS | Alik Tarraf, Marina Tarraf | 199937820109 | QT6HK2556744 | DistroKid screenshot · 2026-09-07 | [cover-170.webp](../assets/covers/by-release/cover-170.webp) |
| SNG-171 | 2025-12-30 | I’M ALIVE | Alik Tarraf | 199937530510 | QT6HL2521340 | Source-normalized | [cover-171.webp](../assets/covers/by-release/cover-171.webp) |
| SNG-172 | 2025-12-31 | С НОВЫМ ГОДОМ МИР | Marina Tarraf (feat. Alik Tarraf) | 199937349631 | QT6HL2591257 | Source-normalized | [cover-172.webp](../assets/covers/by-release/cover-172.webp) |
| SNG-173 | 2026-01-02 | Don’t speak | Alik Tarraf | 199936670354 | QZFYX2677356 | Source-normalized | [cover-173.webp](../assets/covers/by-release/cover-173.webp) |
| SNG-174 | 2026-01-02 | LIFE RACING (soundtrack) | Alik Tarraf | 199936378489 | QZFYY2651675 | Source-normalized | [cover-174.webp](../assets/covers/by-release/cover-174.webp) |
| SNG-175 | 2026-01-03 | ASH REMEMBERS | Alik Tarraf | 199936085394 | QZFYZ2616937 | Source-normalized | [cover-175.webp](../assets/covers/by-release/cover-175.webp) |
| SNG-176 | 2026-01-04 | STAY | Alik Tarraf | 199935827469 | QZFYZ2670515 | DistroKid screenshot · 2026-09-07 | [cover-176.webp](../assets/covers/by-release/cover-176.webp) |
| SNG-177 | 2026-01-06 | Syria-سوريا | Alik Tarraf | 199935071213 | QZFZ32649205 | Source-normalized | [cover-177.webp](../assets/covers/by-release/cover-177.webp) |
| SNG-178 | 2026-01-08 | ПОПЛАЧЬ НА МОЕЙ ГРУДИ | Alik Tarraf | 821451719781 | QZFZ62631227 | Source-normalized | [cover-178.webp](../assets/covers/by-release/cover-178.webp) |
| SNG-179 | 2026-01-08 | ЭТО МЕЛОЧИ | Alik Tarraf | 821451719811 | QZFZ62683800 | DistroKid screenshot · 2026-09-07 | [cover-179.webp](../assets/covers/by-release/cover-179.webp) |
| SNG-180 | 2026-01-09 | AFTER MIDNIGHT / INSTINCT MODE | Marina Tarraf (feat. Alik Tarraf) | 821550870789 | QZFZ62683941 | Source-normalized | [cover-180.webp](../assets/covers/by-release/cover-180.webp) |
| SNG-181 | 2026-01-11 | ЧОМУ Я БЕЗ ДОМУ | Marina Tarraf (feat. Aliana Tarraf) | 821550100572 | QZDA42690879 | Source-normalized | [cover-181.webp](../assets/covers/by-release/cover-181.webp) |
| SNG-182 | 2026-01-12 | DICTATOR MODE | Marina Tarraf (feat. Alik Tarraf) | 821530772225 | QZDA42696455 | Source-normalized | [cover-182.webp](../assets/covers/by-release/cover-182.webp) |
| SNG-183 | 2026-01-12 | I'M HUNGRY | Alik Tarraf | 821530774205 | QZDA42650506 | DistroKid screenshot · 2026-09-07 | [cover-183.webp](../assets/covers/by-release/cover-183.webp) |
| SNG-184 | 2026-01-13 | Тарраф продакшинс поздравляет с Новым Годом | Alik Tarraf | 199934754469 | QZFZ42614354 | Source-normalized | [cover-184.webp](../assets/covers/by-release/cover-184.webp) |
| SNG-185 | 2026-01-27 | TARRAF LIVE SHOW (Live) | Alik Tarraf | 821473229817 | QZHN62624144 | DistroKid dashboard verified | [cover-185.webp](../assets/covers/by-release/cover-185.webp) |
| SNG-186 | 2026-02-07 | THE END | Alik Tarraf & Marina Tarraf | 821473216367 | QZHN62632358 | DistroKid dashboard verified | [cover-186.webp](../assets/covers/by-release/cover-186.webp) |
| SNG-187 | 2026-02-12 | GOODBYE | Marina Tarraf (feat. Alik Tarraf) | 821460245240 | QZHNA2677833 | DistroKid dashboard verified | [cover-187.webp](../assets/covers/by-release/cover-187.webp) |
| SNG-188 | 2026-02-27 | Не продавай себя | Marina Tarraf (feat. Alik Tarraf) | 821317236131 | QZK6F2691254 | DistroKid dashboard verified | [cover-188.webp](../assets/covers/by-release/cover-188.webp) |
| SNG-189 | 2026-02-28 | Continuity / Мы- Переход [Manifesto] | Marina Tarraf (feat. Alik Tarraf) | 821300929286 | QZMEP2665142 | DistroKid dashboard verified | [cover-189.webp](../assets/covers/by-release/cover-189.webp) |
| SNG-190 | 2026-03-21 | Детская боль | Alik Tarraf (feat. Marina Tarraf) | 825715730314 | QZTAS2690128 | DistroKid dashboard verified | [cover-190.webp](../assets/covers/by-release/cover-190.webp) |
| SNG-191 | 2026-04-04 | Я не став поганим | Alik Tarraf | 825626325975 | QZTB72616159 | Public-catalog verified | [cover-191.webp](../assets/covers/by-release/cover-191.webp) |
| SNG-192 | 2026-04-07 | Bèsame, Ya habibi | Alik Tarraf (feat. Marina Tarraf) | 825626671508 | QZTB82636905 | Public-catalog verified | [cover-192.webp](../assets/covers/by-release/cover-192.webp) |
| SNG-193 | 2026-04-09 | Ignis in me | Alik Tarraf | 825583082898 | QZTB92656644 | Public-catalog verified | [cover-193.webp](../assets/covers/by-release/cover-193.webp) |
| SNG-194 | 2026-04-12 | Буллинг | Marina Tarraf (feat. Alik Tarraf) | 825583066386 | QZTBA2623452 | Public-catalog verified | [cover-194.webp](../assets/covers/by-release/cover-194.webp) |
| SNG-195 | 2026-04-15 | Más Cerca / Closer [PART II] | Marina Tarraf (feat. Alik Tarraf) | 825628112610 | QZTB52684532 | DistroKid dashboard verified | [cover-195.webp](../assets/covers/by-release/cover-195.webp) |
| SNG-196 | 2026-04-17 | Позвони родителям | Alik Tarraf | 825484105085 | QZWFF2662937 | Public-catalog verified | [cover-196.webp](../assets/covers/by-release/cover-196.webp) |
| SNG-197 | 2026-04-18 | Desert Dominus | Alik Tarraf (feat. Marina Tarraf) | 825484097878 | QZWFF2663284 | Public-catalog verified | [cover-197.webp](../assets/covers/by-release/cover-197.webp) |
| SNG-198 | 2026-04-19 | Ой, не спи | Alik Tarraf | 825484093344 | QZTBF2666514 | Public-catalog verified | [cover-198.webp](../assets/covers/by-release/cover-198.webp) |
| SNG-199 | 2026-04-29 | Переплавленный | Alik Tarraf | 825353086262 | QZWFQ2609364 | Public-catalog verified | [cover-199.webp](../assets/covers/by-release/cover-199.webp) |
| SNG-200 | 2026-04-30 | Fuego | Alik Tarraf (feat. Marina Tarraf) | 825353054346 | QZWFS2600050 | Public-catalog verified | [cover-200.webp](../assets/covers/by-release/cover-200.webp) |
| SNG-201 | 2026-05-01 | VELCARON — LUX IN TENEBRIS [Dark Ritual] | Alik Tarraf (feat. Marina Tarraf) | 825393870173 | QZWFK2666932 | Public-catalog verified | [cover-201.webp](../assets/covers/by-release/cover-201.webp) |
| SNG-202 | 2026-05-03 | Bullying [TARRAF CARTOON] | Alik Tarraf (feat. Marina Tarraf) | 825353078342 | QZWFR2655484 | Public-catalog verified | [cover-202.webp](../assets/covers/by-release/cover-202.webp) |
| SNG-203 | 2026-05-04 | Комар | Alik Tarraf (feat. Marina Tarraf) | 825393904656 | QZWFK2666876 | Public-catalog verified | [cover-203.webp](../assets/covers/by-release/cover-203.webp) |
| SNG-204 | 2026-05-08 | Пробка [TARRAF CARTOON] | Alik Tarraf (feat. Marina Tarraf) | 825324142805 | QZZ762604656 | Public-catalog verified | [cover-204.webp](../assets/covers/by-release/cover-204.webp) |
| SNG-205 | 2026-05-11 | دربي — Путь Истины | Alik Tarraf (feat. Marina Tarraf) | 825293507599 | QZZ772606090 | Public-catalog verified | [cover-205.webp](../assets/covers/by-release/cover-205.webp) |
| SNG-206 | 2026-05-15 | Марина мій темний вогонь | Alik Tarraf | 825259307911 | QZZ792647093 | Public-catalog verified | [cover-206.webp](../assets/covers/by-release/cover-206.webp) |
| SNG-207 | 2026-05-21 | Відповідай мені | Alik Tarraf (feat. Marina Tarraf) | 825259288326 | QZZ7L2628726 | Public-catalog verified | [cover-207.webp](../assets/covers/by-release/cover-207.webp) |
| SNG-208 | 2026-05-25 | البوميرانغ | Alik Tarraf | 825233033034 | QZZ7P2610480 | Public-catalog verified | [cover-208.webp](../assets/covers/by-release/cover-208.webp) |
| SNG-209 | 2026-05-27 | Born for more - Рождены для большего [LIVE] | Alik Tarraf (feat. Marina Tarraf) | 825254965307 | QZZ7L2635089 | Public-catalog verified | [cover-209.webp](../assets/covers/by-release/cover-209.webp) |
| SNG-210 | 2026-05-29 | Inside | Alik Tarraf | 825233680368 | QZZ7M2682636 | Public-catalog verified | [cover-210.webp](../assets/covers/by-release/cover-210.webp) |
| SNG-211 | 2026-06-01 | يا روح لا تبكي - We are guests [TARRAF LIVE SHOW] | Alik Tarraf (feat. Marina Tarraf) | 882000177995 | QT3EX2647792 | Public-catalog verified | [cover-211.webp](../assets/covers/by-release/cover-211.webp) |
| SNG-212 | 2026-06-03 | Курочка ряба [TARRAF CARTOON] | Marina Tarraf (feat. Alik Tarraf) | 825233594627 | QZZ7P2640453 | Public-catalog verified | [cover-212.webp](../assets/covers/by-release/cover-212.webp) |
| SNG-213 | 2026-06-05 | أيام - Of Fire | Alik Tarraf (feat. Marina Tarraf) | 883071618028 | QT3EZ2625056 | Public-catalog verified | [cover-213.webp](../assets/covers/by-release/cover-213.webp) |
| SNG-214 | 2026-06-19 | Epic Evolution Music (Live Studio Session) | Alik Tarraf & Marina Tarraf | 825192166156 | QZZ7R2695699 | DistroKid dashboard verified | [cover-214.webp](../assets/covers/by-release/cover-214.webp) |
| SNG-215 | 2026-06-21 | Still Yours (LIVE) | Alik Tarraf & Marina Tarraf | 883369720266 | QT3FE2691958 | Public-catalog verified | [cover-215.webp](../assets/covers/by-release/cover-215.webp) |
| SNG-216 | 2025-09-07 | APOCALYPSES | Alik Tarraf (feat. Marina Tarraf) | 199736865578 | QZZ7S2565863 | DistroKid screenshot · 2026-09-07 | [cover-216.webp](../assets/covers/by-release/cover-216.webp) |
| SNG-217 | 2026-10-23 | My Heart Says Goodbye | Alik Tarraf | 881864059270 | QT6G62628340 | DistroKid detail verified | [cover-217.webp](../assets/covers/by-release/cover-217.webp) |
| SNG-218 | 2026-10-10 | Jordan - الأرض المقدسة | Alik Tarraf & Marina Tarraf | 882436167232 | QT6G22657676 | DistroKid detail verified | [cover-218.webp](../assets/covers/by-release/cover-218.webp) |
| SNG-219 | 2026-05-17 | Bite the light (Studio Live Session) | Marina Tarraf | 825254977096 | QZZ7L2614061 | DistroKid detail verified | [cover-219.webp](../assets/covers/by-release/cover-219.webp) |
| SNG-220 | 2015-05-05 | Pick It Up | Manik Bhatheja | 825293554333 | QZZ772605191 | DistroKid detail verified | [cover-220.webp](../assets/covers/by-release/cover-220.webp) |
| SNG-221 | 2026-05-06 | Живая | Marina Tarraf | 825353069494 | QZWFQ2609943 | DistroKid detail verified | [cover-221.webp](../assets/covers/by-release/cover-221.webp) |
| SNG-222 | 2026-04-25 | Удаляй меня | Marina Tarraf | 825500873585 | QZTB92689800 | DistroKid detail verified | [cover-222.webp](../assets/covers/by-release/cover-222.webp) |
| SNG-223 | 2026-04-21 | Не звони мне | Marina Tarraf | 825500876043 | QZTB92686995 | DistroKid detail verified | [cover-223.webp](../assets/covers/by-release/cover-223.webp) |
| SNG-224 | 2026-04-16 | This is goodbye | Marina Tarraf | 825583038222 | QZTB92661671 | DistroKid detail verified | [cover-224.webp](../assets/covers/by-release/cover-224.webp) |
| SNG-225 | 2026-04-10 | Хто ти тепер | Alik Tarraf | 825626537774 | QZTB62662325 | DistroKid detail verified | [cover-225.webp](../assets/covers/by-release/cover-225.webp) |
| SNG-226 | 2026-04-13 | NON STOP (Soundtrack) | Alik Tarraf | 825626650879 | QZTB62644697 | DistroKid detail verified | [cover-226.webp](../assets/covers/by-release/cover-226.webp) |
| SNG-227 | 2026-04-11 | EPIC MODE | Alik Tarraf | 825626657786 | QZTB62641981 | DistroKid detail verified | [cover-227.webp](../assets/covers/by-release/cover-227.webp) |
| SNG-228 | 2026-04-02 | Разлом (Soundtrack) | Marina Tarraf | 825626696211 | QZTB62638190 | DistroKid detail verified | [cover-228.webp](../assets/covers/by-release/cover-228.webp) |
| SNG-229 | 2026-04-05 | 18+ | Alik Tarraf | 825628100518 | QZTB52643580 | DistroKid detail verified | [cover-229.webp](../assets/covers/by-release/cover-229.webp) |
| SNG-230 | 2026-04-08 | Школа жизни | Alik Tarraf | 825682070222 | QZTAZ2642798 | DistroKid detail verified | [cover-230.webp](../assets/covers/by-release/cover-230.webp) |
| SNG-231 | 2026-03-25 | I Will Always Love You | Marina Tarraf | 825758987270 | QZPLR2649825 | DistroKid detail verified | [cover-231.webp](../assets/covers/by-release/cover-231.webp) |
| SNG-232 | 2026-03-03 | Aliana | Alik Tarraf (feat. Marina Tarraf) | 821201623535 | QZNWU2642118 | DistroKid detail verified | [cover-232.webp](../assets/covers/by-release/cover-232.webp) |
| SNG-233 | 2026-03-07 | ОБРАТНЫЙ ОТСЧЁТ | Alik Tarraf | 821275786952 | QZNWR2670507 | DistroKid detail verified | [cover-233.webp](../assets/covers/by-release/cover-233.webp) |
| SNG-234 | 2026-03-15 | Coco Jamboo | Alik Tarraf (feat. Marina Tarraf) | 821300139999 | QZNWR2639595 | DistroKid detail verified | [cover-234.webp](../assets/covers/by-release/cover-234.webp) |
| SNG-235 | 2026-03-04 | ObaTar (Soundtrack) | Alik Tarraf | 821300143590 | QZMEQ2691709 | DistroKid detail verified | [cover-235.webp](../assets/covers/by-release/cover-235.webp) |
| SNG-236 | 2026-03-02 | Не спрашивай потом | Alik Tarraf | 821300623306 | QZMEP2687524 | DistroKid detail verified | [cover-236.webp](../assets/covers/by-release/cover-236.webp) |
| SNG-237 | 2026-03-01 | Он рисует мир | Alik Tarraf | 821300919539 | QZMEP2615493 | DistroKid detail verified | [cover-237.webp](../assets/covers/by-release/cover-237.webp) |
| SNG-238 | 2026-02-26 | После 40 | Alik Tarraf | 821406369436 | QZK6J2673410 | DistroKid detail verified | [cover-238.webp](../assets/covers/by-release/cover-238.webp) |
| SNG-239 | 2026-03-15 | OBARABO (الصحراء العجيبة) | Alik Tarraf | 821406526259 | QZK6J2642099 | DistroKid detail verified | [cover-239.webp](../assets/covers/by-release/cover-239.webp) |
| SNG-240 | 2026-02-24 | Мой путь (LIVE) | Alik Tarraf | 821430004266 | QZK6H2644131 | DistroKid detail verified | [cover-240.webp](../assets/covers/by-release/cover-240.webp) |
| SNG-241 | 2026-03-11 | OBARABO (DOMINÉ) | Alik Tarraf | 821430010977 | QZK6K2667471 | DistroKid detail verified | [cover-241.webp](../assets/covers/by-release/cover-241.webp) |
| SNG-242 | 2026-03-03 | OBARABO (ANRA LUMÉ) | Alik Tarraf | 821430023823 | QZK6K2667447 | DistroKid detail verified | [cover-242.webp](../assets/covers/by-release/cover-242.webp) |
| SNG-243 | 2026-02-24 | I Rise | Alik Tarraf | 821430038339 | QZK6K2665001 | DistroKid detail verified | [cover-243.webp](../assets/covers/by-release/cover-243.webp) |
| SNG-244 | 2026-02-23 | Любовь | Alik Tarraf | 821430041100 | QZK6K2662665 | DistroKid detail verified | [cover-244.webp](../assets/covers/by-release/cover-244.webp) |
| SNG-245 | 2026-02-22 | La vita | Alik Tarraf | 821438386760 | QZK6N2680514 | DistroKid detail verified | [cover-245.webp](../assets/covers/by-release/cover-245.webp) |
| SNG-246 | 2026-02-21 | Democrats | Alik Tarraf | 821438394826 | QZK6N2680321 | DistroKid detail verified | [cover-246.webp](../assets/covers/by-release/cover-246.webp) |
| SNG-247 | 2026-02-19 | Моё нутро | Alik Tarraf | 821438401593 | QZK6N2674431 | DistroKid detail verified | [cover-247.webp](../assets/covers/by-release/cover-247.webp) |
| SNG-248 | 2026-02-18 | حبك مو لعبة | Alik Tarraf & Marina Tarraf | 821438418959 | QZK6L2688208 | DistroKid detail verified | [cover-248.webp](../assets/covers/by-release/cover-248.webp) |
| SNG-249 | 2026-02-17 | Más Cerca / Closer | Alik Tarraf (feat. Marina Tarraf) | 821438428491 | QZK6L2688089 | DistroKid detail verified | [cover-249.webp](../assets/covers/by-release/cover-249.webp) |
| SNG-250 | 2026-02-14 | الليلة مجنونة | Alik Tarraf | 821438443043 | QZK6N2667269 | DistroKid detail verified | [cover-250.webp](../assets/covers/by-release/cover-250.webp) |
| SNG-251 | 2026-02-11 | Tell me why | Alik Tarraf | 821438452847 | QZK6N2663590 | DistroKid detail verified | [cover-251.webp](../assets/covers/by-release/cover-251.webp) |
| SNG-252 | 2026-02-16 | Все хорошо (Live) | Marina Tarraf | 821440980352 | QZK6N2617663 | DistroKid detail verified | [cover-252.webp](../assets/covers/by-release/cover-252.webp) |
| SNG-253 | 2026-02-25 | OBARAE (TARRAF RITUAL SONG) | Alik Tarraf & Marina Tarraf | 821460277760 | QZHNA2667994 | DistroKid detail verified | [cover-253.webp](../assets/covers/by-release/cover-253.webp) |
| SNG-254 | 2026-02-20 | OBARABO STI-ME (TARRAF RITUAL SONG) | Marina Tarraf | 821460278200 | QZHN82648633 | DistroKid detail verified | [cover-254.webp](../assets/covers/by-release/cover-254.webp) |
| SNG-255 | 2026-02-09 | ParaDiseDox | Alik Tarraf | 821470289883 | QZHN62670941 | DistroKid detail verified | [cover-255.webp](../assets/covers/by-release/cover-255.webp) |
| SNG-256 | 2026-02-07 | СРОК ИСТЁК | Alik Tarraf | 821470325635 | QZHN62666102 | DistroKid detail verified | [cover-256.webp](../assets/covers/by-release/cover-256.webp) |
| SNG-257 | 2026-02-05 | AVE LUMEN AETERNUM (Ritual Song) | Alik Tarraf | 821470350026 | QZHN62662026 | DistroKid detail verified | [cover-257.webp](../assets/covers/by-release/cover-257.webp) |
| SNG-258 | 2026-01-29 | Выбираю себя | Alik Tarraf & Marina Tarraf | 821470729174 | QZHN52672795 | DistroKid detail verified | [cover-258.webp](../assets/covers/by-release/cover-258.webp) |
| SNG-259 | 2026-02-15 | OBARABO (TARRAF RITUAL SONG ) | Alik Tarraf | 821473122996 | QZHN42693830 | DistroKid detail verified | [cover-259.webp](../assets/covers/by-release/cover-259.webp) |
| SNG-260 | 2026-02-13 | Жизнь не игра | Alik Tarraf | 821473147562 | QZHN42684128 | DistroKid detail verified | [cover-260.webp](../assets/covers/by-release/cover-260.webp) |
| SNG-261 | 2026-01-31 | We are different | Alik Tarraf | 821473208997 | QZHN42675661 | DistroKid detail verified | [cover-261.webp](../assets/covers/by-release/cover-261.webp) |
| SNG-262 | 2026-01-29 | ОСТАВЛЮ СЛЕД | Alik Tarraf | 821473224478 | QZHN42671448 | DistroKid detail verified | [cover-262.webp](../assets/covers/by-release/cover-262.webp) |
| SNG-263 | 2026-02-03 | Still here ((TARRAF LIVE SHOW)) | Marina Tarraf | 821473813634 | QZHN42674434 | DistroKid detail verified | [cover-263.webp](../assets/covers/by-release/cover-263.webp) |
| SNG-264 | 2026-02-01 | Good morning world | Alik Tarraf | 821473829871 | QZHN32622972 | DistroKid detail verified | [cover-264.webp](../assets/covers/by-release/cover-264.webp) |
| SNG-265 | 2026-02-10 | Detonate | Alik Tarraf | 821473835087 | QZHN32622943 | DistroKid detail verified | [cover-265.webp](../assets/covers/by-release/cover-265.webp) |
| SNG-266 | 2026-02-02 | МАРИНА | Alik Tarraf | 821473841729 | QZHN32620913 | DistroKid detail verified | [cover-266.webp](../assets/covers/by-release/cover-266.webp) |
| SNG-267 | 2026-02-03 | Страсть Боль Прощение | Alik Tarraf | 821473846700 | QZHN32620896 | DistroKid detail verified | [cover-267.webp](../assets/covers/by-release/cover-267.webp) |
| SNG-268 | 2026-02-06 | Пока мы живы | Alik Tarraf (feat. Marina Tarraf) | 821473850189 | QZHN42663366 | DistroKid detail verified | [cover-268.webp](../assets/covers/by-release/cover-268.webp) |
| SNG-269 | 2026-02-08 | Я слышу тебя | Alik Tarraf | 821473856082 | QZHN32618130 | DistroKid screenshot · 2026-09-07 | [cover-269.webp](../assets/covers/by-release/cover-269.webp) |
| SNG-270 | 2026-01-25 | ЗА ЧТО | Alik Tarraf | 821473977428 | QZES92694771 | DistroKid screenshot · 2026-09-07 | [cover-270.webp](../assets/covers/by-release/cover-270.webp) |
| SNG-271 | 2026-02-04 | Детство ((New Version)) | Alik Tarraf | 821500164579 | QZES92663296 | DistroKid detail verified | [cover-271.webp](../assets/covers/by-release/cover-271.webp) |
| SNG-272 | 2026-01-30 | King's move | Alik Tarraf | 821500845171 | QZES82639913 | DistroKid screenshot · 2026-09-07 | [cover-272.webp](../assets/covers/by-release/cover-272.webp) |
| SNG-273 | 2026-01-28 | Смотри это Алик | Alik Tarraf | 821520484602 | QZDA82684848 | DistroKid detail verified | [cover-273.webp](../assets/covers/by-release/cover-273.webp) |
| SNG-274 | 2026-01-26 | Life is not a game | Alik Tarraf | 821520512831 | QZDA82681109 | DistroKid detail verified | [cover-274.webp](../assets/covers/by-release/cover-274.webp) |
| SNG-275 | 2026-01-23 | Огонь в крови | Alik Tarraf | 821526627324 | QZDA62676404 | DistroKid detail verified | [cover-275.webp](../assets/covers/by-release/cover-275.webp) |

## Provenance

Derived from the TARRAF PRODUCTIONS master discography and rights workbook supplied for this repository update. Source coverage was audited on 2026-07-25. Seven previously missing UPC values, the release date for `APOCALYPSES`, the joint primary-artist credits for `THE END` and `Epic Evolution Music (Live Studio Session)`, the exact version-title punctuation for the latter release, and the explicit-content designation for `Не продавай себя` were verified directly against first-party DistroKid dashboard records on 2026-09-04. A complete dashboard overview capture from `My Heart Says Goodbye` through `SWINGS` was reviewed the same day; after reconciliation with the 216 previously canonical singles it confirmed 59 additional distinct single products. Their first-party detail records were subsequently transcribed and validated, bringing the canonical singles register to 275 products. The Arabic title `حبك مو لعبة` was corrected from the detail record and remains distinct from `أيام - Of Fire`. On 2026-09-07, 23 additional DistroKid release-detail screenshots and owner clarifications were reconciled in the [follow-up review](distrokid-reconciliation-2026-09-07.md). The exact artist strings for GODDESS, Sila Lyubvi, New World, BANINA BANINA YALLA TARRAF and studio STILL YOURS replace the earlier featured-artist normalization. Marina’s primary-artist attribution is confirmed for PROSTO, Vyshel Alik Pogulyat, Shtorm i Lyubov and POSSESSED. Only public catalog facts needed for identification are published here; private source paths, correspondence, and unsupported fields are excluded.

---

**TARRAF PRODUCTIONS® · EPIC EVOLUTION MUSIC**

© 2025–2026 TARRAF PRODUCTIONS. All rights reserved.
