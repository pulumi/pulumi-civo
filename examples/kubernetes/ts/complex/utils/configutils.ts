import * as pulumi from "@pulumi/pulumi";
import {hasText} from "./textutils";

export function getStringOrDefault(config: pulumi.Config, key: string, defaultValue: string): string {
    let val = config.get(key);

    if (val === undefined) {
        return defaultValue;
    }
    else if (!hasText(val)) {
        return defaultValue;
    }
    else {
        return val;
    }
}

export function getBooleanOrDefault(config: pulumi.Config, key: string, defaultValue: boolean): boolean {
    let val = config.getBoolean(key);

    if (val === undefined) {
        return defaultValue;
    }
    else {
        return val;
    }
}

export function getNumberOrDefault(config: pulumi.Config, key: string, defaultValue: number): number {
    let val = config.getNumber(key);

    if (val === undefined) {
        return defaultValue;
    }
    else {
        return val;
    }
}
