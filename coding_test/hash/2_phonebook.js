function solution(phone_book) {
    phone_book.sort()

    for (let i = 0; i < phone_book.length - 1; i++) {
        if (phone_book[i + 1].startsWith(phone_book[i])) {
            return false;
        }
    }
    return true;
}

// some으로 순회, 인덱스를 받아 쓰는 방법
// return !phoneBook.sort().some((t,i)=> {
//     if(i === phoneBook.length -1) return false;