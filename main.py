def paginate(total_pages, current_page, boundaries, around):

    pages = list()
    all_pages = list(range(1, total_pages + 1))

    for page in all_pages:
        if page <= boundaries or page > total_pages - boundaries:
            pages.append(page)
            continue

        if (page >= current_page - around and
                page < current_page or
                current_page + around >= page and
                page >= current_page):
            pages.append(page)
        elif len(pages) == 0 or pages[-1] != '...':
            pages.append('...')

    return pages

if __name__ == '__main__':
    print('Example 1:', paginate(5, 4, 1, 0))
    print('Example 2:', paginate(10, 4, 2, 2))
