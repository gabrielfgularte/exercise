def paginate(total_pages, current_page, boundaries, around):

    pages = list()

    if boundaries > 0:
        pages += list(range(1, boundaries + 1))

    if around > 0:
        pages += list(range(current_page - around, current_page + (around + 1)))
    else:
        pages.append(current_page)

    if boundaries > 0:
        pages += list(range(total_pages - boundaries + 1, total_pages + 1))

    pages = list(dict.fromkeys(pages))

    previous_page = 1
    first_gap = None
    last_gap = None

    for i, page in enumerate(pages):
        if page - previous_page == 0:
            previous_page += 1
        else:
            if first_gap:
                last_gap = i + 1
                break
            first_gap = i
            previous_page = page + 1

    if first_gap:
        pages.insert(first_gap, '...')
    elif pages[0] != 1:
        pages.insert(0, '...')

    if last_gap:
        pages.insert(last_gap, '...')
    elif pages[-1] != total_pages:
        pages.append('...')

    return pages

if __name__ == '__main__':
    print('Example 1:', paginate(5, 4, 1, 0))
    print('Example 2:', paginate(10, 4, 2, 2))
