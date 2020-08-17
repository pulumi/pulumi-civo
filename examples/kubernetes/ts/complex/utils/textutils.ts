export function hasText(text: string | undefined): boolean {
    return !((text === undefined) || (text === null) || (text === ""));
}
