package kata
import (
    "strings"
)
func ToJadenCase(str string) string {
  str = strings.Title(strings.ToLower(str))
  return str 
}
